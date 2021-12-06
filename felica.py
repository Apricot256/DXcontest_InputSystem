from time import sleep
from requests import post
from gpiozero import LED 
from nfc import ContactlessFrontend, connect


url = 'https://api.dxcontest.sora210.dev'   #server url
pin = 26    #output gpio pin
delay1 = 1000 #main loop delay [ms]
delay2 = 500 #after reading delay [ms]

class felica():

    def __init__(self):
        self.clf = ContactlessFrontend('usb')
        self.gpio = LED(pin)
        self.payload = {'id':0}

    #get student infomation
    def f_read(self):
        tag = self.clf.connect(rdwr={'on-connect': lambda tag: False})
        #read successfly
        if tag:
            tag = str(tag).split() 
            tag = tag[4]
            self.payload['id'] = tag
            return True
        #read fault
        else:
            return False

    #emission beep sound (pi-pi)
    def beep(self):
        for i in range(2):
            self.gpio.on()
            sleep(delay2/(1000*4))
            self.gpio.off()
            sleep(delay2/(1000*4))

    #post information
    def post(self):
        r = post(url, data=self.payload)


if __name__ == '__main__':
    fe = felica()
    while True:
        if fe.f_read():
            fe.post()
            fe.beep()
        sleep(delay1)