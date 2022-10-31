# List Part-1 (Tutorial 23)

subjects = ["C", "C++", "Java", "Python", "Android", "OS"]
print(subjects)
print(subjects[0]) #print the value of index 0
print(subjects[2:]) #print the value of index 2 to last index
print(subjects[-1]) #print the 1st index from end (Output: OS)

print("Python" in subjects) #return true cause Python is in the list
print("Swift" in subjects) #return false cause Swift is not in the list

print("Swift" not in subjects) #return true

print(subjects + ["Swift", 27]) #Swift & 27 are added in the list

print(subjects * 3) #print the items of the list 3 times
