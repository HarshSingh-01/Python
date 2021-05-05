# Printing Stars in Right angle triangle.
a = int(input("Enter the number of rows: "))
for i in range(0,a+1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()