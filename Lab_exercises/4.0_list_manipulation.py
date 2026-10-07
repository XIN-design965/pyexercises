"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What my list is about, and what I computed from it:


# Your code below
# Cities where the business operates
business_cities = [
    "Shanghai",
    "Hangzhou",
    "Guangzhou",
    "Beijing",
    "Wuhan",
    "Kunming",
    "Tianjing",
    "Nanjing"
]

# Display the whole list
print("The whole list:", business_cities)

# Display one city of my choice
print("One selected city:", business_cities[2])

# Display the cities in alphabetical order
sorted_cities = sorted(business_cities)
print("The sorted list:", sorted_cities)

# Calculate the number of cities
number_of_cities = len(business_cities)
print("The business operates in", number_of_cities, "cities.")