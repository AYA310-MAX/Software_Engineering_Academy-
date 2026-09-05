student = {
    "name": "Aya",
    "age": 22,
    "course": "Software Engineering",
    "languages": ["Python", "Java", "JavaScript"],
    "is_graduated": False
}

print(student["name"])
print(student["course"])

for language in student["languages"]:
    print(language)

    if "Python" in language:
        print("Python is being learned!")
        
for key, value in student.items():
           print(key, value)