# Dictionaries (Tutorial 32)

#Dictonary is a data structure in python. Key -> Value pair
#Name -> "Tasnimul Hasan"
#Email -> samithasan@gmail.com
#Age -> 22

studentId = {
    "101" : "Tasnimul Hasan",
    "102" : "Anisul Islam",
    "103" : "Shakib Al Hasan",
    "104" : "Tamim Iqbal",
}
#print(studentId["101"])
print(studentId.get("101")) #another method to access
print(studentId.get("106","Not a valid key")) #we set default value = "Not a valid key"
