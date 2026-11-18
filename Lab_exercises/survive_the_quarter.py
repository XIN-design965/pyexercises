# Student: XIN ZHAO
# Group: B
#
# 1. What goes in?
# - The scenarios come from scenarios_B.csv.
# - The file uses semicolons as separators and contains 14 columns.
# - Each row starts with a scenario number and a situation.
# - Options A, B and C each contain choice text, a budget change, a reputation
#   change and a feedback message.
# - Budget and reputation changes are positive, negative or zero integers.
# - The player also enters a name, a difficulty level and one choice per day.
# 
# 2. What happens during one day?
# - The game displays the day number, budget and reputation.
# - It displays the situation and choices A, B and C.
# - It asks for a choice and asks again if the answer is invalid.
# - It retrieves and unpacks the tuple for the selected option.
# - It applies the budget and reputation changes.
# - It limits reputation to a maximum of 100.
# - It displays the feedback and records the move in the history.
# - It stops the game if budget or reputation reaches zero or less.
#
# 3. What comes out?
# - During the game, the player sees the situations, choices and feedback.
# - The player sees every budget and reputation change.
# - At the end, the program displays the remaining budget and reputation.
# - If a gauge reaches zero, it displays the reason why the player was fired.
# - If the player survives, it displays the final score and title.
# - It displays the best and worst reputation moves.
# - It appends name, budget, reputation, title and date to results.csv.

#
# 4. What could go wrong?
# - An empty name causes the program to ask for the name again.
# - An invalid difficulty or choice causes the program to ask again.
# - A missing scenario file produces a clear error and stops the program safely.
# - A wrong CSV header or invalid number produces a clear data error.
# - A budget or reputation value at zero or less ends the game immediately.
# - If results.csv cannot be written, the result stays on screen and the program
#   displays a saving warning.
#
# Feature choice: difficulty mode. It lets the player choose easy (15,000 EUR)
# or hard (6,000 EUR), which makes replaying the same scenario pool interesting.


import csv
import random
from datetime import date
from pathlib import Path


# Keep file paths next to this script so it runs from any working directory.
BASE_DIR = Path(__file__).resolve().parent
SCENARIO_FILE = BASE_DIR / "scenarios_B.csv"
RESULTS_FILE = BASE_DIR / "results.csv"

STARTING_REPUTATION = 50
MAX_REPUTATION = 100
DAYS_PER_GAME = 10

EXPECTED_FIELDS = [
    "Num",
    "Situation",
    "A_Choice",
    "A_Money",
    "A_Buzz",
    "A_Reaction",
    "B_Choice",
    "B_Money",
    "B_Buzz",
    "B_Reaction",
    "C_Choice",
    "C_Money",
    "C_Buzz",
    "C_Reaction",
]


# Convert one CSV row into a dictionary containing three option tuples.
def build_scenario(row, line_number):
    try:
        scenario_number = int(row["Num"])
        options = {}

        for letter in ("A", "B", "C"):
            options[letter] = (
                row[f"{letter}_Choice"].strip(),
                int(row[f"{letter}_Money"]),
                int(row[f"{letter}_Buzz"]),
                row[f"{letter}_Reaction"].strip(),
            )
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(
            f"Invalid data on CSV line {line_number}: {error}"
        ) from error

    situation = row["Situation"].strip()
    if not situation or any(not option[0] for option in options.values()):
        raise ValueError(f"Missing situation or choice text on CSV line {line_number}.")

    return {
        "number": scenario_number,
        "situation": situation,
        "options": options,
    }


# Read every Group B scenario with the semicolon format found in the file.
def load_scenarios(file_path):
    scenarios = []

    with file_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")

        if reader.fieldnames != EXPECTED_FIELDS:
            raise ValueError(
                "The scenario header does not match the expected Group B format."
            )

        for line_number, row in enumerate(reader, start=2):
            scenarios.append(build_scenario(row, line_number))

    if len(scenarios) < DAYS_PER_GAME:
        raise ValueError(
            f"At least {DAYS_PER_GAME} scenarios are required, but only "
            f"{len(scenarios)} were loaded."
        )

    return scenarios


# Ask until the player enters a non-empty name.
def ask_player_name():
    while True:
        name = input("Player name: ").strip()
        if name:
            return name
        print("Please enter a name.")


# Optional feature D: choose the budget before the game starts.
def ask_difficulty():
    while True:
        answer = input("Difficulty - easy (15,000 EUR) or hard (6,000 EUR): ")
        answer = answer.strip().lower()

        if answer in ("easy", "e"):
            return 15000, "easy"
        if answer in ("hard", "h"):
            return 6000, "hard"

        print("Please type easy, hard, e or h.")


# Show one day in the same order every time.
def display_day(day_number, budget, reputation, scenario):
    print(f"\n--- Day {day_number} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
    print(scenario["situation"])

    for letter in ("A", "B", "C"):
        option_text = scenario["options"][letter][0]
        print(f"  {letter}: {option_text}")


# Reject every answer except A, B or C, while accepting lower-case input.
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Please type A, B or C.")


# Apply one option and return a tuple that the caller unpacks.
def apply_choice(budget, reputation, option):
    _, budget_change, reputation_change, _ = option
    new_budget = budget + budget_change
    new_reputation = min(MAX_REPUTATION, reputation + reputation_change)
    return new_budget, new_reputation


# Decide whether the player was fired or earned a surviving title.
def calculate_result(budget, reputation):
    if budget <= 0 and reputation <= 0:
        return "Fired", None, "budget and reputation reached zero or less"
    if budget <= 0:
        return "Fired", None, "budget reached zero or less"
    if reputation <= 0:
        return "Fired", None, "reputation reached zero or less"

    score = reputation + budget // 200

    if score < 95:
        title = "Eternal Intern"
    elif score <= 119:
        title = "Growth Hacker"
    elif score <= 139:
        title = "CMO Material"
    else:
        title = "Viral Legend"

    return title, score, None


# Use tuple comparison: reputation change is the first value in each history row.
def find_best_and_worst_moves(history):
    best_move = max(history)
    worst_move = min(history)
    return best_move, worst_move


# Add one result row and create the header only when the file is new or empty.
def save_result(file_path, name, budget, reputation, title):
    needs_header = not file_path.exists() or file_path.stat().st_size == 0

    with file_path.open("a", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        if needs_header:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# Run the ten-day game and keep one history tuple for every played day.
def play_game(name, starting_budget, difficulty, scenarios):
    budget = starting_budget
    reputation = STARTING_REPUTATION
    history = []

    random.shuffle(scenarios)
    selected_scenarios = scenarios[:DAYS_PER_GAME]

    print(f"\nWelcome, {name}. Difficulty: {difficulty}.")
    print("Survive ten days without letting either gauge reach zero.")

    for day_number, scenario in enumerate(selected_scenarios, start=1):
        display_day(day_number, budget, reputation, scenario)
        choice = ask_choice()
        option = scenario["options"][choice]
        choice_text, budget_change, reputation_change, feedback = option

        budget, reputation = apply_choice(budget, reputation, option)
        history.append(
            (reputation_change, day_number, choice_text, budget_change)
        )

        print(feedback)
        print(
            f"Budget {budget_change:+d} EUR, "
            f"Reputation {reputation_change:+d}"
        )

        if budget <= 0 or reputation <= 0:
            break

    title, score, fired_reason = calculate_result(budget, reputation)
    best_move, worst_move = find_best_and_worst_moves(history)

    print("\n" + "=" * 30)
    if fired_reason:
        print(f"Game over: you were fired because {fired_reason}.")
    else:
        print("Quarter survived!")
        print(f"Final score: {score}")
        print(f"{name}, your title: {title}")

    print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
    print(
        f'Best move: day {best_move[1]}, "{best_move[2]}" '
        f"({best_move[0]:+d} reputation)"
    )
    print(
        f'Worst move: day {worst_move[1]}, "{worst_move[2]}" '
        f"({worst_move[0]:+d} reputation)"
    )

    return budget, reputation, title


# Keep file and keyboard errors outside the game logic so the script ends cleanly.
def main():
    print("SURVIVE THE QUARTER")

    try:
        name = ask_player_name()
        starting_budget, difficulty = ask_difficulty()
        scenarios = load_scenarios(SCENARIO_FILE)
        budget, reputation, title = play_game(
            name, starting_budget, difficulty, scenarios
        )
    except (EOFError, KeyboardInterrupt):
        print("\nGame cancelled. No result was saved.")
        return
    except FileNotFoundError:
        print(f"Scenario file not found: {SCENARIO_FILE.name}")
        return
    except (csv.Error, UnicodeError, ValueError) as error:
        print(f"Could not load the scenarios: {error}")
        return

    try:
        save_result(RESULTS_FILE, name, budget, reputation, title)
        print(f"Saved in {RESULTS_FILE.name}")
    except (OSError, csv.Error) as error:
        print(f"The game finished, but the result could not be saved: {error}")


if __name__ == "__main__":
    main()
