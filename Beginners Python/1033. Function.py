# Function (Tutorial 36)

#Function 2 types. 1) Library Function, 2) User defined function
def add(x,y):
    sum = x + y
    print(sum)

def addition(x,y,z):
    sum = x + y + z
    print(sum)

def sub(x,y):
    result = x - y
    print(result)

def message():
    print("No parameter")

add(10,20)
addition(80,20,10)
sub(80,20)
message()