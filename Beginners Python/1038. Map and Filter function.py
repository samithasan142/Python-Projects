# map and filter function (Tutorial 41)

#map fucntion mainly can received a function and list
def square(x):
    return x*x

num = [1,2,3,4,5]
result = list(map(square, num))
print(result)

#filter function

num2 = [1,2,3,4,5]

result2 = list(filter(lambda x: x%2==0, num2))
print(result2) #Output: [2,4]
