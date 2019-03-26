# print string.count('abc','c')
my_str = "abcde"
print(my_str.find("c"))
str_size = len(my_str)
# print my_str.find("e")
list = []
for i in range(str_size):
    reversed_i = str_size - i - 1
    list.append(my_str[reversed_i])

print("".join(list))
print(my_str.replace('a', 'x'))
print(my_str)
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
