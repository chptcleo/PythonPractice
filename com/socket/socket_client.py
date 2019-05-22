'''
@author: Administrator
'''
import socket

def send_request():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))
    print(s.recv(1024).decode('utf-8'))
    for data in ['kobe', 'james', 'wade']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send('exit')
    s.close()


if __name__ == '__main__':
    send_request()