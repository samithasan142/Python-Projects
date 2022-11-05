# Reading a file (Tutorial 45)

file = open("student.txt", "r")
#print(file.readable())
#print(file.writable())

'''
text = file.read()
print(text)
size = len(text)
print(size)
'''

'''
text2 = file.readlines()
print(text2)
'''

'''
text3 = file.readlines() [0]
print(text3)
'''

for line in file:
    print(line) #print all line using for loop

file.close()
