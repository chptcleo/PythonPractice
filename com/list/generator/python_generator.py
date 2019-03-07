def generate():
    yield 1
    yield 2
    yield 3

if __name__ == "__main__":
    g = generate()
    for n in g:
        print n