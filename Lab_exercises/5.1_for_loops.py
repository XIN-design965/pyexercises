"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The list of business cities created in Exercise 4.0.
# 2. Process:Loop through every city and calculate the length of its name.
# 3. Out:One line for each city showing its position, name, and name length.
# 4. What I compute for each item, and why it is worth showing:I computed the length of each city name. The reader learns each city's position in the list and how many characters its name contains.

# Your code below
# List copied from Exercise 4.0
business_cities = [
    "Shanghai",
    "Hangzhou",
    "Guangzhou",
    "Beijing",
    "Wuhan",
    "Kunming",
    "Tianjin",
    "Nanjing"
]

# Process every item in the list
for position, city in enumerate(business_cities, start=1):
    name_length = len(city)
    print(f"{position}. {city} has {name_length} characters.")