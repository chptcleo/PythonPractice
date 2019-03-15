from collections import Counter

counter = Counter()
for x in 'whatwhatisthat':
    counter[x] = counter[x] + 1
print(counter)
