'''
@author: Wallace Chen
'''
def lines(parse_file):
    for line in parse_file: yield line
    yield '\n'
    
def blocks(parse_file):
    block = []
    for line in lines(parse_file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
                
if __name__ == '__main__':
    pass