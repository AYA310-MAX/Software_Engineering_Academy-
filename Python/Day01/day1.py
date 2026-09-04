print("=" * 50)
print("Software Engineering Academy")
print("Day 1 - Student profile Generator")
print("=" * 50)

name = input("Hello! What is your name: \n")
age = int(input("What is your age: \n"))
degree = input("What degree are you doing: \n")
favourite_language = input("What is your favourite coding language: \n")
dream_job = input("What is your dream Job: \n")

print("\n" + "=" * 50)
print("STUDENT PROFILE")
print("=" * 50)

print(f"Name: {name.title()}")
print(f"Age: {age}")
print(f"degree: {degree.title()}")
print(f"Favourite Language: {favourite_language.title()}")
print(f"Dream Job: {dream_job.title()}")

birth_year = 2026 - age

print(f"Estimated Birth Year: {birth_year}")

if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")

print("=" * 50)
print("Thank you for using the Student Profile Generator!")

"""
Exercise: 2
"""
print("\n" + "=" * 50)
print("Exercise 2 - Area and Perimeter Calculator")
print("=" * 50)


width = float(input("Enter the width of the rectangle: \n"))
height = float(input("Enter the height of the rectangle: \n"))

area = width * height
perimeter = 2 * (width + height)

print(f"\n The Area of the Rectangle is: {area}")
print(f"The perimeter of the Rectange is: {perimeter}")


print("\n" + "=" * 50)
print("\n" + "=" * 50)


#Eample 
#print("Welcome to the Software Engineering Academy!")

#name = input("What is your name? ")
#age = int(input("How old are you? "))

#print(f"Hello {name}!")
#print(f"You are {age} years old.")



#Exercise 1 

print ("Lets us get to know you better!!")
name = "Aya"
age = 21

print(f"Hello! {name}!")
print(f"You are, {age}, years old.")

favourite_food = input(f"What is your favourite food {name}?")
favourite_programming_language = input(f"What is your favourite programming language {name}? ")

print(f"Wow! {name}, you are so interesting at {age} years old.")

age_next = int(input(f"How old are you next year {name}? "))

#if, else statements 
if age_next >= 18:
    print("You are an adult!")
else:
    print("You are a minor")

print(f"Wow, {name}")
print(f"You are old now!!")