"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A sentence entered by the user.
# 2. Process:Remove spaces from both ends and apply four different transformations.
# 3. Out:Four transformed versions of the sentence are displayed.
# 4. My four transformations, and when each is useful:
# strip() + upper(): removes spaces at both ends and creates uppercase text for emphasis.
# strip() + lower(): removes spaces at both ends and standardizes text for comparison.
# strip() + replace(): removes spaces at both ends and replaces spaces with underscores for filenames.
# strip() + title(): removes spaces at both ends and capitalizes each word for titles.


# Your code below
# ask user for a sentence
sentence = input("Enter a sentence: ")

# remove spaces at both ends, and convert all characters to uppercase
print("Upper()     :", sentence.strip().upper())

# remove spaces at both ends, and convert all characters to lowercase
print("Lower()     :", sentence.strip().lower())

# remove spaces at both ends, and replace spaces with underscores
print("Replace()   :", sentence.strip().replace(" ", "_"))

# remove spaces at both ends, and capitalise the first letter of each word
print("Title()     :", sentence.strip().title())