# List Comprehensions (Tutorial 42)

num = [1,2,3,4,5]
result = list(map(lambda x: x*x, num))
print(result)

#[expression for item in list]
num2 = [1,2,3,4,5]
result2 = [x*x for x in num2]
print(result2)

num3 = [1,2,3,4,5]
result3 = [x for x in num if x%2==0]
print(result3)