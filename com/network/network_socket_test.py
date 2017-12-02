'''
@author: Wallace Chen
'''
import socket

def test_socket():
    s = socket.socket()
    host_name = socket.gethostname()
    s.connect((host_name,1234))
    print s.recv(1234)


if __name__ == '__main__':
    test_socket()
    test_socket()
    test_socket()
    test_socket()
    test_socket()
    test_socket()