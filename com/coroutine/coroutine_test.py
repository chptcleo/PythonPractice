def consumer():
    r = ''
    print('[CONSUMER] Outside loop')
    while True:
        n = yield r
        print('[CONSUMER] n is %s' % n)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

    
c = consumer()
print('[MAIN] First c is %s' % c)
produce(c)
