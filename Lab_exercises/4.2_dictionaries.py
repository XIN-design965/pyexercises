"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a product, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A product dictionary and a field name entered by the user.
# 2. Process:Read, update, remove, search for, and display dictionary fields.
# 3. Out:The requested information and every remaining product field and value.
# 4. My object, my five fields, and why those:My object is a software product. The five fields are product ID, product name, city, product manager, and monthly sales. They identify the product, show where it operates, who manages it, and how well it performs.


# Your code below
product = {
    "product_id": "HZ001",
    "product_name": "Metallic_gate_software",
    "city": "Hangzhou",
    "product_manager": "ZHAO Xin",
    "monthly_sales": 120000
}

# Read one field
print("Product name:", product["product_name"])

# Change one field
product["monthly_sales"] = 125000
print("Updated monthly sales:", product["monthly_sales"])

# Remove one field
removed_product_manager = product.pop("product_manager")
print("Removed product manager:", removed_product_manager)

# Ask for a field and handle a field that does not exist
requested_field = input("Enter a field name: ")

if requested_field in product:
    print(requested_field, ":", product[requested_field])
else:
    print("That field does not exist.")

# Display every remaining field and its value
print("Remaining product information:")

for field, value in product.items():
    print(field, ":", value)