'''
@author: Wallace Chen
'''
import urllib

def test_urllib():
    webpage = urllib.urlopen('http://www.baidu.com')
    text = webpage.read()
    print text


if __name__ == '__main__':
    test_urllib()