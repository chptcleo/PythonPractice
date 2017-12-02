import re

class Handler:

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)
        
    def start(self, name):
        self.callback('start_', name)
        
    def end(self, name):
        self.callback('end_', name)
        
    def sub(self,name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result
        return substitution
    
if __name__ == '__main__':
    handler = Handler()
    print handler.sub('emphasis')
    print re.sub(r'\*(.+?)\*', handler.sub('emphasis'), 'This *is* a test')
        