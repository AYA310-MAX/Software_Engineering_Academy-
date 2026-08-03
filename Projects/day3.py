'''
Mini Project 1
Grade Calculator

Ask for a student's mark and display:

75–100 → Distinction
50–74 → Pass
Below 50 → Fail
'''
print("=" * 40)
print("GRADE CALCULATOR")
print("=" * 40)

mark = float(input("Enter your mark: "))

print()

if mark >= 75:
    print("Distinction")
elif mark >= 50:
    print("Pass")
else:
    print("Fail")

'''
🚀 Mini Project 2
Movie Ticket Checker

Ask:

Age

If:

18 or older → "You may watch the movie."
Under 18 → "You are too young."
'''
print("=" * 40)
print("MOVIE TICKET CHECKER")
print("=" * 40)

age = int(input("Enter your age: "))

if age >= 18:
    print("You may watch the movie.")
else:
    print("You are too young.")
'''
🚀 Mini Project 3 ⭐
Login System

Create a username and password.

username = "admin"
password = "python123"

Ask the user to enter both.

If both are correct:

Login Successful

Otherwise:

Incorrect username or password.
'''

print("=" * 40)
print("Login System")
print("=" * 40)

username = print(input("Enter your username: "))
password = print(input("Enter your password: "))

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Incorrect username or password.")    
    



'''
Mini Project 4: Banking Withdrawal Checker

Requirements:

Ask for:

Account Balance
Withdrawal Amount

If enough money:

Withdrawal Approved

Else:

Insufficient Funds
'''

print("=" * 40)
print("Banking Withdrawal Checker")
print("=" * 40)

balance = float(input("Please may you enter your account balance: \n"))

withdrawal = float(input("Please may you enter your withdrawal amount: \n"))

if withdrawal <= balance:
    print("Withdrawal approved.")

else:
    print("Withdrawal denied. Insufficient funds.")
    


    '''
    Ask for:

Username
Password
Age

Allow access only if:

Username is correct
Password is correct
User is 18 or older
    '''


    username = input("Please enter username: \n ")
    password = input("Please enter password: \n ")
    age = int(input("Please enter your age: \n "))

    if username == "admin" and password == "python123" and age >= 18:
        print("Access granted.")
    else:
        print("Access denied.") 