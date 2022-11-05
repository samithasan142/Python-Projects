# Lambda Functions (Tutorial 40)

#A function without name (Anonymous Function)
#Not powerful as Named Function
#It can work with single expression/ single line of code

def calculate(a,b):
    return a*a + 2*a*b + b*b
print(calculate(2,3))

#lambda parameter : expression
result = (lambda a,b : a*a + 2*a*b + b*b) (2,3)
print(result)

result2 = (lambda x : x*x*x) (2)
print(result2)
