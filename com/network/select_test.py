'''
@author: Wallace Chen
'''
import socket, select
from wx.py.dispatcher import disconnect

def test_select():
    s = socket.socket()
    host_name = socket.gethostname()
    s.bind((host_name, 1234))
    s.listen(5)
    inputs = [s]
    while True:
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            if r is s:
                c, addr = s.accept()
                print 'Got connection from', addr
                inputs.append(c)
            else:
                try:
                    data = r.recv(1024)
                    disconnect = not data
                except socket.error:
                    disconnect= True
                    
                if disconnect:
                    print r.getpeername(), "disconnect"
                    inputs.remove(r)
                else:
                    print data

if __name__ == '__main__':
    test_select()
