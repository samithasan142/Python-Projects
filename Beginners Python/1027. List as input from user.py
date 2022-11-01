# List as input from user (Tutorial 30)

# Website for more practise: pynative.com
n = input("Enter a text of numbers: ")
# 10 20 30 40
list = n.split() # 10, 20, 30, 40
sum = 0

for num in list:
    sum = sum + int(num)

print(sum)

numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a string including numbers: ") #My text is 123

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numOfLetters = numOfLetters + 1
    elif x >= '0' and x <= '9':
        numOfDigits = numOfDigits + 1
    elif x == ' ':
        numOfWords = numOfWords + 1

print("Number of letters: ",numOfLetters)
print("Number of digits: ",numOfDigits)
print("Number of words: ",numOfWords+1)