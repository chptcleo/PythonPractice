

def generate_list(L):
    return [str.lower(x) for x in L if isinstance(x, str)]


if __name__ == "__main__":
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = generate_list(L1)
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('pass!')
    else:
        print('fail!')
    
