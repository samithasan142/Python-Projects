# List Part-2 (Tutorial 24)

subjects = ["C", "C++", "Java", "Python", "C++", "Android"]
print(len(subjects)) #Output: 5

subjects.append("OS") #append OS in the list
print(subjects)

subjects.insert(2, "FLC") #insert FLC in index 2
print(subjects)

subjects.remove("Java") #remove Android from the list
print(subjects)

subjects.sort() #sort the subjects according to dictonary
print(subjects)

subjects.reverse() #sort into decending order
print(subjects)

subjects.pop() #pop the last item of the list
print(subjects)

subjects2 = subjects.copy() #copy the items of subject
print(subjects2)

position = subjects.index("C++") #print the position of C++
print(position)

cnt = subjects.count("C++") #count the number of items
print(cnt)

subjects.clear() #clear the list
print(subjects)
