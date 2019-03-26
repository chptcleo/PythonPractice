'''
@author: Wallace Chen
基本功能：一是探测一组主机是否在线；其次是扫描 主机端口，嗅探所提供的网络服务；还可以推断主机所用的操作系统
'''
from nmap import nmap

nm = nmap.PortScanner()
nm.scan('192.168.1.104-106', '22,80')
print('command: ' + nm.command_line())
# print 'scaninfo: ', nm.scaninfo()
# print 'hosts: ', nm.all_hosts()
# print 'host name: ', nm['192.168.1.106'].hostname()
# print 'state: ', nm['192.168.1.106'].state()
# print 'protocol: ', nm['192.168.1.106'].all_protocols()
# print 'all tcp: ', nm['192.168.1.106'].all_tcp()
# print 'tcp: ', nm['192.168.1.106'].tcp(22)
