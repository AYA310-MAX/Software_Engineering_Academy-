'''
Mini Project 1: Multiplication Table

Ask the user for a number and display its multiplication table.

Example:

Enter a number: 7

Output:

7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
...
7 × 10 = 70
'''

number = int(input("Enter a number: "))
for i in range(1, 11): 
    print(i, "x", number, "=", i * number)

'''
Mini Project 2: Countdown Timer

Display:

10
9
8
7
6
5
4
3
2
1
Blast Off! 🚀

Use a while loop.
'''
count = 10

while count >= 1:
    print(count)
    count -= 1 

'''
Mini Project 3: Password Attempts

The correct password is:

Python2026

Allow the user 3 attempts.

If they enter the correct password:

Welcome!

Otherwise:

Access Denied

This combines loops and conditional statements. 
'''



    