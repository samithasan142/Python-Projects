# Logical Operator (Tutorial 18)

num1 = 30
num2 = 20
num3 = 40
if num1 > num2 and num1 > num3:
        print(num1)
elif num2 > num1 and num2 > num3:
        print(num2)
else:
    print(num3)

ch = 'a' #vowel = a,e,i,o,u
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")
