languages = ["Python", "Java", "JavaScript", "Dart", "SQL" ]

print(languages)
print(languages[0])
print(languages[3])
print(languages[4])

languages[2] = "TypeScript"

languages.append("Go")
languages.remove("Java")

length = len(languages)
print(languages)
print(length)

print(languages)

for language in languages:
 if language == "Python" or language == "JavaScript" or language == "Dart":
    print(language)


languages = ["Python", "Java", "JavaScript", "Dart", "SQL"]

for language in languages:

 if language in  ["Java", "JavaScript", "Dart"]:
    print(language)

languages = ("React", "JavaScript", "HTML","CSS")

languages[0] = "Python"
print(languages)

