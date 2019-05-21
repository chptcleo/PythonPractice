'''
@author: Administrator
'''
import socket, time, threading

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 9999))
    s.listen(5)
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=process_request, args=(sock, addr))
        t.start()
        
        
def process_request(sock, addr):
    print('Get connection from %s ' % str(addr))
    sock.send('Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s closed' % str(addr))
            
        


if __name__ == '__main__':
    start_server()