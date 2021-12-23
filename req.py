from requests import post, get
#r = post('https://api.dxcontest.sora210.dev', data="hogehoge")
r = get('https://api.dxcontest.sora210.dev/health')
print(r.text)