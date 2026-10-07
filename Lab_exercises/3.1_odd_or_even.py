"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:An integer N entered by the user.
# 2. Process:Validate N, then use a loop and the modulus operator to check each number.
# 3. Out:Every number from 1 to N is displayed as either odd or even.
# 4. What happens on 0, on a negative number, on a very large number:The program displays an error and asks again. Only numbers from 1 to 518 are accepted.


# Your code below
while True:
    # Get a number from user and convert to integer
    n = int(input("Enter a number N: "))
    # Check boundary conditions
    if n == 0:
        print("N cannot be zero. Please enter a positive integer.")
    elif n < 0:
        print("N cannot be negative. Please enter a positive integer.")
    elif n > 518:
        print("N is too large. Please enter a number from 1 to 518.")
    else:
        break

# Run only after the user enters a valid number
for num in range(1, n + 1):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")