# Returning value from Function (Tutorial 37)

def add(a,b):
    sum = a + b
    return sum

result = add(20,30)
print("Result = ",result)

def large(a,b):
    if a>b:
        return a
    else:
        return b

print(large(100,30))
