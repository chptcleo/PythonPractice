#!D:\Python27\python.exe
import cgi
form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print 'Content-type: text/plain'
print
print 'Hello, %s!' % name