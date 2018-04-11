class Person:
    pass
print Person
print type(Person)
print Person()
print type(Person)

class Foo(object):
    pass
print Foo
print type(Foo)
print Foo()
print type(Foo())

Pig = type('Pig',(),{})
print Pig
print Pig()