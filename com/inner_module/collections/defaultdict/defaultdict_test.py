from collections import defaultdict

dd = defaultdict(lambda:'n/a')
dd[1] = 'x'
dd[2] = 'y'
print(dd[1])
print(dd[3])
d1 = dict({'b':'m','c':'n'})
d1['a'] = 'x'
print(d1['a'])
print(d1['c'])