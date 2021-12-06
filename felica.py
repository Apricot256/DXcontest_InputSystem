from time import sleep
from requests import post
from gpiozero import LED 
import nfc


url = 'https://api.dxcontest.sora210.dev'
pin = 26
delay = 300 #after reading delay [ms]

class felica():
    def __init__(self):
        self.clf = nfc.ContactlessFrontend('usb')
        self.gpio = LED(pin)
        self.url = url
        self.payload = {'id':0}


    #get student infomation
    def f_read(self):
        tag = self.clf.connect(rdwr={'on-connect': lambda tag: False})
        tag = str(tag).split() 
        tag = tag[4]
        #success reading
        if tag:
            self.payload['id'] = tag
            return True
        #can't read
        else:
            return False

    def beep(self):
        for i in range(2):
            self.gpio.on()
            sleep(delay/(1000*2))
            self.gpio.off()


    #send information
    def post(self):
        r = post(self.url, data=self.payload)


if __name__ == '__main__':
    fe = felica(url)
    while True:
        if fe.f_read():
            fe.post()
            fe.beep()