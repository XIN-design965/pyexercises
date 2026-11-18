"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -
# -
# -
# -

# 1. In:
# 2. Process, problem by problem:
# 3. Out:
# 4. How I decide which word is the last name:


# Your code below
# What is wrong with names.txt (found by reading it, not by guessing):
# - There are two empty lines that do not contain a name.
# - Some lines start with extra spaces.
# - The first names do not use consistent capitalisation.
# - The last names do not use consistent capitalisation.
# - One name has three words, including the surname particle "van".

# 1. In:
# - The input is names.txt.
# - It contains one person's name per non-empty line.
# - The lines contain inconsistent spaces and capitalisation.

# 2. Process, problem by problem:
# - Remove spaces at the beginning and end of each line.
# - Ignore lines that are empty after removing spaces.
# - Split each valid line into separate words.
# - Normalise the capitalisation of every name.
# - Keep surname particles such as "van" in lower case.
# - Sort the cleaned names by the last word of each line.

# 3. Out:
# - The output is cleaned_names.txt.
# - It contains eight cleaned names, one per line, sorted by last name.
# - The original names.txt file is not modified.

# 4. How I decide which word is the last name:
# - The file follows the format "first name followed by last name".
# - Therefore, for a two-word line, the second word is the last name.
# - More generally, I use the final word as the sorting key.
# - In "Guido van Rossum", Rossum is the sorting key and "van" stays in the
#   displayed name as part of the surname.

from pathlib import Path


# Store both files next to this Python script.
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "names.txt"
OUTPUT_FILE = BASE_DIR / "cleaned_names.txt"

# These particles normally remain lower-case inside a name.
LOWERCASE_PARTICLES = {"van", "von", "de", "da", "del"}


# Clean one non-empty line and return one consistently formatted name.
def clean_name(line):
    words = line.strip().split()
    cleaned_words = []

    for index, word in enumerate(words):
        lowercase_word = word.lower()

        if index > 0 and lowercase_word in LOWERCASE_PARTICLES:
            cleaned_words.append(lowercase_word)
        else:
            cleaned_words.append(lowercase_word.capitalize())

    return " ".join(cleaned_words)


# Return the final word so that sort() orders the list by last name.
def last_name_key(full_name):
    return full_name.split()[-1].casefold()


# Read the original file without changing it.
def load_and_clean_names(file_path):
    cleaned_names = []
    input_line_count = 0

    with file_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            input_line_count += 1
            if line.strip():
                cleaned_names.append(clean_name(line))

    return cleaned_names, input_line_count


# Write a different file, with one name on each line.
def save_names(file_path, names):
    with file_path.open("w", encoding="utf-8") as output_file:
        for name in names:
            output_file.write(name + "\n")


def main():
    try:
        names, input_line_count = load_and_clean_names(INPUT_FILE)
    except FileNotFoundError:
        print(f"Input file not found: {INPUT_FILE.name}")
        return

    names.sort(key=last_name_key)
    save_names(OUTPUT_FILE, names)

    print(f"Read {input_line_count} input lines.")
    print(f"Saved {len(names)} cleaned names to {OUTPUT_FILE.name}.")


if __name__ == "__main__":
    main()