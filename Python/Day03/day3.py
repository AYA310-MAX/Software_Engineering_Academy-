print("=" * 40)
print("Software Engineering Academy")
print("=" * 40 + "\n")
print ("=" * 40)
print("Day 3 - Age Tracker")
print("=" * 40)

name = input ("Enter your name: ")
age = int(input("Enter your age: "))

print()

if age >=18:
    print(f"Welcome, {name.title()}!")
    print("You are an adult.")
else:
    print(f"Hello, {name.title()}!")
    print("You are a minor.")

print("\nThank you for using the Age Checker!")

mark = int(input("Please amy you enter your mark: \n"))

if mark >= 75:
    print("Well done! You have achieved a distinction.")

elif mark >=50:
    print("Pass")

else: 
    print("Fail")



#LOGICAL OPERATORS

# and
age = 20 
has_id = True

if age >= 18 and has_id:
    print("Welcome! You are allowed to enter.")

else: 
    print("Sorry! You are not allowed to enter.")

#or

is_student = True
is_staff = True

if is_student or is_staff:
    print("Good Moning! You are allowed to enter.")
    

