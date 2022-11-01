# Tuples (Tutorial 33)

#Tuples is a data structure.
# We can change the value of list but we can't change the value of Tuples
#Tuples is more faster than list

#In case of List, we use [ ] --> Third Bracket
#In case of Dictionaries, we use { } --> Second Bracket
#In case of Tuples, we use ( ) --> First Bracket

students = (
    ("Tasnimul Hasan",22,3.55), #Tuples inside tuples
    "Shakib Al Hasan",
    "Tamim Iqbal",
)
#students[0] = "Moinul Islam" --> We can't change the value
print(students[0])
print(students[1:]) #print the value from index 1 to end
print(students)
