"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:An integer from 1 to 100 entered by the user.
# 2. Process:Compare each guess with the secret number and count each attempt.
# 3. Out:A high, low, or correct message, followed by a summary.
# 4. My stop condition, my attempt limit, my summary:The loop stops when the user guesses 66 or uses all five attempts. The summary shows the attempts used and whether the number was guessed.


# Your code below
secret_number = 66
max_attempts = 5
attempts = 0
guessed_correctly = False

while attempts < max_attempts:
    guess = int(input("Guess a number from 1 to 100: "))
    attempts = attempts + 1

    if guess < 1 or guess > 100:
        print("Please enter a number from 1 to 100.")
    elif guess == secret_number:
        guessed_correctly = True
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

# Display a summary
print("Summary:")
print(f"Attempts used: {attempts}")

if guessed_correctly:
    print("You guessed the correct number.")
else:
    print(f"You did not guess the number. It was {secret_number}.")