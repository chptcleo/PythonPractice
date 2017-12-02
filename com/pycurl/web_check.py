import pycurl
import os, sys

URL = 'http://www.baidu.com'
c = pycurl.Curl()

c.setopt(pycurl.URL, URL)
c.setopt(pycurl.CONNECTTIMEOUT, 5)
c.setopt(pycurl.TIMEOUT, 5)
c.setopt(pycurl.NOPROGRESS, 1)
c.setopt(pycurl.FORBID_REUSE, 1)
c.setopt(pycurl.MAXREDIRS, 1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)

index_file = open(os.path.dirname(os.path.realpath(__file__)) + '/content.txt', 'wb')
c.setopt(pycurl.WRITEHEADER, index_file)
c.setopt(pycurl.WRITEDATA, index_file)

try:
    c.perform()
except Exception, e:
    print 'connect error:', str(e)
    index_file.close()
    c.close()
    sys.exit()
    
NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print 'http code:', HTTP_CODE
print 'DNS interpret time:', NAMELOOKUP_TIME
print 'build connect time:', CONNECT_TIME
print 'prepare transfer time:', PRETRANSFER_TIME
print 'start transfer time:', STARTTRANSFER_TIME
print 'end transfer time:', TOTAL_TIME
print 'data package size:', SIZE_DOWNLOAD
print 'http header size:', HEADER_SIZE
print 'download speed:', SPEED_DOWNLOAD

index_file.close()
c.close()
