f = lambda x: x * x
print f(2)
l = [1, 2, 4, -3, -2, 0]
print map(lambda x: x * x, l)
print filter(lambda x: x < 0, l)
print reduce(lambda x, y: x + y, l)
l2 = [('z', 26), ('b', 2), ('h', 8), ('a', 1)]
print sorted(l2, key=lambda x: x[1])
