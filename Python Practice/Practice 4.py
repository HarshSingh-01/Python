# This is to write our file
file = open('file.txt','w')

file.write('Python\n')
file.write('How I am going to write a file')
file.close() # for closing the file

# This is going to read our file again
file = open('file.txt','r')
f = file.readlines()

newlist =[]
for line in f:
    newlist.append(line.strip())

print(newlist)
