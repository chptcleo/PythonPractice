'''
@author: Wallace Chen
'''
import socket
from SocketServer import TCPServer, StreamRequestHandler, ThreadingMixIn

class Server(ThreadingMixIn, TCPServer):pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thanks for your connection')

def test_serversocket():
    s = socket.socket()
    host_name = socket.gethostname()
    
    s.bind((host_name, 1234))
    s.listen(5)
    while True:
        c, address = s.accept()
        print 'Got connection from', address
        c.send('Thanks for your connection')
        c.close()

if __name__ == '__main__':
#     test_serversocket()
    host_name = socket.gethostname()
#     server = TCPServer((host_name, 1234), Handler)
    server = Server((host_name, 1234), Handler)
    server.serve_forever()
