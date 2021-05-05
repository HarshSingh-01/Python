from collections import deque

a = deque('Tim')
a.clear()
a.extend('xyz')
a.extendleft('cba')
a.rotate(6)
a.reverse()
print(a)