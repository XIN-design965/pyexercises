"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The list of business cities created in Exercise 4.0.
# 2. Process:Process: Create reordered lists without changing the original list.
# 3. Out:The cities in four different orders, followed by the original list.
# 4. My four orders, and which ones modify the original:The four orders are original, alphabetical, reverse alphabetical, and reversed original order. sorted() creates new lists, while reverse() modifies a copied list in place. The original list is never modified.


# Your code below
# Original list from Exercise 4.0
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

# 1. Display the original order
print("Original order:", business_cities)

# 2. Display the cities in alphabetical order
alphabetical_cities = sorted(business_cities)
print("Alphabetical order:", alphabetical_cities)

# 3. Display the cities in reverse alphabetical order
reverse_alphabetical = sorted(business_cities, reverse=True)
print("Reverse alphabetical order:", reverse_alphabetical)

# 4. Display the cities in reversed original order
reversed_cities = business_cities.copy()
reversed_cities.reverse()
print("Reversed original order:", reversed_cities)

# Prove that the original list has not changed
print("Original list at the end:", business_cities)