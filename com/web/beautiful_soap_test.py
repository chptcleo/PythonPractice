'''
@author: Wallace Chen
'''
from urllib import urlopen
from bs4 import BeautifulSoup

def test_bs():
    text = urlopen('http://python.org/community/jobs').read()
    soup = BeautifulSoup(text)
    
    jobs = set()
    for header in soup('h3'):
        links = header('a', 'reference')
        if not links: continue
        link = links[0]
        jobs.add('%s (%s)' % (link.string, link['href']))
        
    print '\n'.join(sorted(jobs, key=lambda s: s.lower()))
    


if __name__ == '__main__':
    test_bs()