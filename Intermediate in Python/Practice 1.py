li = [1,2,3,4,5,6,7,8,9,10]
def func(x):
    return x**3

#print(list(map(func,li)))
print([func(i) for i in li if i%2 == 0])
