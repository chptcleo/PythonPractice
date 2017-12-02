'''
@author: Wallace Chen
'''
from urllib import urlopen
from HTMLParser import HTMLParser

class Scraper(HTMLParser):
    
    in_h3 = False
    in_link = False
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h3':
            print 'start <h3>'
            self.in_h3 = True
        if tag == 'a' and 'href' in attrs:
            print 'start <a>'
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']
            
        
    def handle_data(self, data):
        if self.in_link:
            print 'process data'
            self.chunks.append(data)
        
    def handle_endtag(self, tag):
        if tag == 'h3':
            print 'end <h3>'
            self.in_h3 = False
        if tag == 'a':
            print 'end <a>'
            if self.in_link:
                print 'print chunks'
                print '%s, (%s)' % (' '.join(self.chunks), self.url)
            self.in_link = False
            
    

if __name__ == '__main__':
    text = urlopen('http://python.org/community/jobs').read()
    parser = Scraper()
    parser.feed(text)
    parser.close()