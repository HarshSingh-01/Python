from collections import Counter

c = Counter(a=1,b=2,c=0,d=-2)
d = Counter(['a','b','b','c'])
print(c+d)
d.clear()
print(d)
d.update(c)
print(d)