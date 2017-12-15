class BaseHandler:
    def successor(self, successor):
        self.successor = successor

class ScoreHandler1(BaseHandler):
    def handle(self, request):
        if request > 90 and request <= 100:
            return "A+"
        else:
            return self.successor.handle(request)

class ScoreHandler2(BaseHandler):
    def handle(self, request):
        if request > 80 and request <= 90:
            return "A"
        else:
            return self.successor.handle(request)

class ScoreHandler3(BaseHandler):
    def handle(self, request):
        if request > 70 and request <= 80:
            return "B+"
        else:
            return "unsatisfactory result"

class Client:
    def __init__(self):
        h1 = ScoreHandler1()
        h2 = ScoreHandler2()
        h3 = ScoreHandler3()
        h1.successor(h2)
        h2.successor(h3)

        requests =  {'zhangsan': 78,
                    'lisi': 98,
                    'wangwu': 82,
                    'zhaoliu': 60}
        for name, score in requests.iteritems():
            print '{} is {}'.format(name, h1.handle(score))

if __name__== "__main__":
    client = Client()