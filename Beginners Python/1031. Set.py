# Set (Tutorial 34)

#Set is a data structure.
#Set is an unordered collection of item
#We can't store duplicate value in set
#A set can be created using - 1) curly braces, 2) set function

num = {1,2,3,4,5}
print(num)

num2 = {1,2,3,4,5,5}
print(num2) #print 5 one times, can't print the duplicate value

num3 = set([4,5,6]) #2nd method
print(num3)
num3.add(7) #add element in set
print(num3)
num3.remove(7) #remove element in set
print(num3)

print(7 in num3) #False, cause 7 isn't in the set
print(4 in num3) #True, cause 4 is in the set

print(4 not in num3) #False, cause 4 is in the set

num4 = {1,2,3,4,5}
num5 = {4,5,6,7}
print(num4 | num5) #Union of set
print(num4 & num5) #Intersection of set
print(num4 - num5) #Difference of set
