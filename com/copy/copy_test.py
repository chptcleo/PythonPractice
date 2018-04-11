import copy

a = [1,2,2,34,'hello',['x','y']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(99)
a[5].append('z')
print '%s' % a
print '%s' % b
print '%s' % c
print '%s' % d
print b.pop()
b.remove(2)
print b

e = 2
f = e
e = 3
print e
print f