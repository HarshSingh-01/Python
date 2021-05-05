from collections import namedtuple
Point = namedtuple('Point',{'x':0, 'y':0, 'z':0})
newP = Point(1,2,3)
print(newP.x,newP.y,newP.z)
print(newP._fields)

newP = newP._replace(x=6)
print(newP)

p = Point._make(['a','b','c'])
print(p)