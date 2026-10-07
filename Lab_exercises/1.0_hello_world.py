"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a string of my name.
# 2. Process: use for loop to iterate, add line number before the text each iteration.
# 3. Out:numberd lines showing my name.
# 4. My message, and why: "XIN ZHAO". This is my name, simple and meaningful for me.


# Your code below
repeat_times = 3
text = "XIN ZHAO"
for line_num in range(1, repeat_times + 1):
    print(f"{line_num}. {text}")
