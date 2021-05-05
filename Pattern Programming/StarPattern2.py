# *
# ***
# *****

a =  int(input("Enter the number of Rows: "))
k = 1
for i in range(0,a):
    for j in range(1, k+1):
        print("*", end=" ")
    k = k+2
    print()