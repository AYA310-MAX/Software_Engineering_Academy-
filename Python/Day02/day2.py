print("=" * 40) #Understanding the First Line
#print("=" * 40)
#What happens?
#Python takes the equal sign (=) and repeats it 40 times.
#Think of it like this:
#"="
#↓
#========================
#Output:
#========================================
#Why do this?
#It makes your program look cleaner and easier to read.
#Professional developers often add headers like this.



print("Software Engineering Academy")
print("Day 2 - Student Introduction")
print("=" * 40)

name = input("Hello! What is your name? \n")
 #What is \n?
#\n means,Move to a new line.
age = int(input("Please enter your age: \n"))
food = input ("What is your favourite food? ")

print("\n\n\n----- PROFILE -----")
print(f"Name: {name.title()}")
print(f"Age: {age} ")
print(f"Favourite Food: {food.title()}")

next_year = age + 1

print(f"\nNext year you will be {next_year} years old.")

print("\nThank you for using this program!\n\n\n")
