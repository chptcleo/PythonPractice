import dns.resolver
import os
import httplib

iplist = []
appdomain = '163.com'

def get_iplist(domain=''):
    a_dns = dns.resolver.query('163.com', 'A')
    for i in a_dns.response.answer:
        for j in i.items:
            iplist.append(j.address)

def check(ip):
    check_url = ip + ':80'
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(check_url)
    conn.request('GET', '/', headers = {'Host': appdomain})
    r = conn.getresponse()
    page_content = r.read(15)
    if page_content == '<!doctype html>':
        print ip, " [OK]"
    else:
        print ip, " [ERROR]"

if __name__=='__main__':
    get_iplist(appdomain)
    for ip in iplist:
        check(ip)
