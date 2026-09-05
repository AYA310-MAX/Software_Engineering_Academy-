'''
Dictionaries 
'''
student = {
    "name": "Aya",
    "age": 21,
    "Course": "Software Engineering",
    "is_graduated": False
}

print(student["name"])
print(student["age"])
print(student["is_graduated"])

student["age"] = 22

student["city"] = "Johannesburg"
student["university"] ="Eduvos"
print(student)

student = {
    "name": "Aya",
    "age": 22,
    "course": "Software Engineering",
    "city": "Johannesburg"
}

for key in student:
    print(student[key])