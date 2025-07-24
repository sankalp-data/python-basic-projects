import json
from pprint import pprint
import calendar
from datetime import datetime

filepath = r"Habit_Tracker\habit_tracker_file.json"

def open_to_write(file):
    '''Open file for writing'''
    with open(filepath, "w") as f:
        json.dump(file, f, indent=4)

def loading():
    '''Load Data from habit_tracker_file.json'''
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # If file does not exist or is empty/corrupted

def add_habit():
    '''Add new habit(s)'''
    content = loading()
    try:
        how_many_habits = int(input("How many habits do you want to add?\n➡️  "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    date = input("Date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validate format
    except ValueError:
        print("❌ Invalid date format! Use YYYY-MM-DD")
        return

    if date not in content:
        content[date] = {}

    for _ in range(how_many_habits):
        habit = input("Habit: ").strip()
        if habit:
            content[date][habit] = False

    open_to_write(content)
    print("✅ Habits saved successfully!")

def marking_habit():
    '''Mark a habit as completed'''
    content = loading()

    if not content:
        print("❌ Nothing in habit tracker file.")
        return

    date = input("Date (YYYY-MM-DD): ").strip()
    try:
        valid_date = datetime.strptime(date, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("❌ Invalid date syntax! Use YYYY-MM-DD")
        return

    if valid_date in content:
        pprint(content[valid_date])
        ask = input("Which habit do you want to mark as ✅ Completed?\n➡️  ").strip()
        if ask in content[valid_date]:
            content[valid_date][ask] = True
            open_to_write(content)
            print("✅ Habit marked as complete!")
        else:
            print("❌ Habit not found!")
    else:
        print("❌ No such date found!")

def view_calendar():
    '''Display calendar with habit completion status'''
    content = loading()

    try:
        year = int(input("Enter Year: "))
        if year < 1 or year > 9999:
            print("❌ Please enter a year between 1 and 9999")
            return

        month = int(input("Enter Month (1-12): "))
        if month < 1 or month > 12:
            print("❌ Please enter a valid month (1-12)")
            return

    except ValueError:
        print("❌ Please enter a valid number!")
        return

    days_in_month = calendar.monthrange(year, month)[1]
    print(f"\n📅 Habit Tracker Calendar\n{calendar.month_name[month]} {year}")
    print("Mo Tu We Th Fr Sa Su")

    start_day = calendar.monthrange(year, month)[0]
    day_counter = 1
    row = ["  "] * start_day  # Fill initial blanks

    while day_counter <= days_in_month:
        day_str = f"{day_counter:02}"
        full_date = f"{year}-{month:02}-{day_str}"

        if full_date in content:
            if all(content[full_date].values()):
                label = f"{day_str}✅"
            else:
                label = f"{day_str}❌"
        else:
            label = f"{day_str}  "

        row.append(label)

        if len(row) == 7:
            print("  ".join(row))
            row = []

        day_counter += 1

    if row:
        print("  ".join(row))

def edit_or_delete():
    '''Edit or delete habits from the JSON file'''
    content = loading()

    date = input("Date (YYYY-MM-DD): ").strip()
    try:
        valid_date = datetime.strptime(date, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("❌ Invalid date syntax! Use YYYY-MM-DD")
        return

    if valid_date not in content:
        print("❌ No such date found!")
        return

    print(f"\nHabit details on {valid_date}:")
    pprint(content[valid_date])

    choice = input("Enter:\n1 to edit a habit\n2 to delete a habit\n➡️  ").strip()

    if choice == "1":
        habit_to_edit = input("Enter habit name to edit: ").strip()

        if habit_to_edit in content[valid_date]:

            new_name = input("Enter new habit name: ").strip()

            content[valid_date][new_name] = content[valid_date].pop(habit_to_edit)

            open_to_write(content)

            print("✅ Habit name updated successfully!")

        else:
            print("❌ No such habit found!")

    elif choice == "2":

        habit_to_delete = input("Enter habit name to delete: ").strip()

        if habit_to_delete in content[valid_date]:

            del content[valid_date][habit_to_delete]

            if not content[valid_date]:

                del content[valid_date]  # Clean up empty date entry

            open_to_write(content)

            print("🗑️ Habit deleted successfully!")
        else:
            print("❌ No such habit found!")

    else:
        print("❌ Invalid choice! Please enter 1 or 2.")




        

