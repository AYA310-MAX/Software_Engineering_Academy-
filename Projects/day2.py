'''
Mini Project 1
Personal Profile Generator

Ask the user for:

Name
Age
Favourite Movie
Favourite Food
Dream Job

Display everything neatly.
'''
print("=" * 40)
print("Academy Personal Profile Generator")
print("=" * 40)

print("Hello! Welcome Student")
print("Please answer the following questions to generate your personal profile.\n") 


name = input("What is your name?\n")
age = int(input("What is your age?\n"))
food = input("What is your favourite food?\n")
dream_job = input("What is your dream job?\n")

print("\n----- Personal profile -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favourite Food: {food}")
print(f"Dream Job: {dream_job}")


'''

🚀 Mini Project 2
Simple Shopping Calculator

Ask for:

Product Name
Price
Quantity

Calculate:

Total Cost

Example:

Laptop

Price: R12000

Quantity: 2

Total: R24000
⭐ Bonus

Add VAT (15%).
'''
print ("=" * 40)
print("Simple Shopping Calculator")
print("=" * 40)

product_name = input("What is the product name?\n")
price = float(input("What is the price?\n"))
quantity = int(input("What is the quantity?\n"))

total_cost = price * quantity
vat = total_cost * 0.15
final_total = total_cost + vat

print(f"Product Name: {product_name}")
print(f"Price: R{price}")
print(f"Quantity: {quantity}")
print(f"Total Cost: R{total_cost}")
print(f"VAT (15%): R{vat}")
print(f"Final Total: R{final_total}")

'''

🚀 Mini Project 3
BMI Calculator

Ask for:

Height
Weight

Calculate:

BMI = weight / height²

Then tell the user if they are:

Underweight
Healthy
Overweight

'''
print("=" * 40)
print("BMI Calculator")
print("=" * 40)

height = float(input("What is your height in meters?\n"))
weight = float(input("What is your weight in kilograms?\n"))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You are healthy.")
else:
    print("You are overweight.")
