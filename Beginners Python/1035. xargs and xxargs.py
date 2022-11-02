# xxargs and xxxargs (Tutorial 38)

#xargs
def student(*details): #Here number of parameters are not fixed
    print(details)

student(101, "Anis")
student(102, "Anis", 3.75)

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)

#xxargs
def student(id, name):
    print(id, name)

student(id=101, name="Anis") #key value pair

def student(**details):
    print(details)
    print(details["id"])
    print(details["name"])

student(id=101, name="Anis") #key value pair