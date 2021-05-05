# lambda with map method
li = [1,2,3,4,5,6,7,8,9]

a = list(map(lambda x: x+2, li))

b = list(filter(lambda x: x%2 != 0, li))

print(a)
print(b)