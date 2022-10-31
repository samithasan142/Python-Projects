# For Loop (Tutorial 26)

num = [10,20,30,40,50]
print(num)
sum = 0

index = 0
n = len(num)

while index<n:
    print(num[index])
    index = index + 1
print("End of While Loop")

for x in num:
    print(x)
    sum = sum + x
print("The sum is : ",sum)
