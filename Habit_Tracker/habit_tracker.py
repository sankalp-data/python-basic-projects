import json
import calendar
from pprint import pprint
from datetime import datetime, date

filepath = r"Habit_Tracker\habit_tracker_file.json"

def open_to_write(file):
    '''Open file for writing'''
     
    with open(filepath, "w") as f:
        json.dump(file, f, indent=4)



def loading():
    '''Load Data from JSON'''

    try:
        with open(filepath, "r") as f:
            return json.load(f)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return {}



def add_habit():
    '''Add new habit(s)'''

    content = loading()

    try:
        how_many = int(input("How many habits do you want to add?\n➡  "))

    except ValueError:
        print("❌ Please enter a valid number!")
        return

    today = date.today().isoformat()

    if today not in content:
        content[today] = {}

    for _ in range(how_many):
        habit = input("Habit: ").strip()

        if habit:
            content[today][habit] = False

    open_to_write(content)

    print("✅ Habits saved successfully!")




def marking_habit():
    '''Mark a habit as completed'''

    content = loading()

    if not content:
        print("❌ Nothing in habit tracker.")
        return

    input_date = input("Date (YYYY-MM-DD): ").strip()

    try:
        valid_date = datetime.strptime(input_date, "%Y-%m-%d").date().isoformat()

    except ValueError:
        print("❌ Invalid date syntax! Use YYYY-MM-DD")
        return

    if valid_date in content:

        pprint(content[valid_date])

        ask = input("Which habit do you want to mark as ✅ Completed?\n➡  ").strip()

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
        month = int(input("Enter Month (1-12): "))

        if not (1 <= month <= 12):
            raise ValueError
        
    except ValueError:
        print("❌ Invalid input! Year or Month is incorrect.")
        return

    days_in_month = calendar.monthrange(year, month)[1]

    print(f"\n📅 Habit Tracker Calendar\n{calendar.month_name[month]} {year}")

    print("Mo Tu We Th Fr Sa Su")

    start_day = calendar.monthrange(year, month)[0]

    row = ["  "] * start_day

    for day in range(1, days_in_month + 1):

        day_str = f"{day:02}"

        full_date = f"{year}-{month:02}-{day_str}"

        if full_date in content:

            label = f"{day_str}✅" if all(content[full_date].values()) else f"{day_str}❌"

        else:

            label = f"{day_str}  "

        row.append(label)

        if len(row) == 7:

            print("  ".join(row))

            row = []

    if row:

        print("  ".join(row))




def edit_or_delete():
    '''Edit or delete habits from the JSON file.'''

    content = loading()

    input_date = input("Date (YYYY-MM-DD): ").strip()

    try:
        valid_date = datetime.strptime(input_date, "%Y-%m-%d").date().isoformat()

    except ValueError:
        print("❌ Invalid date syntax! Use YYYY-MM-DD")
        return


    if valid_date not in content:
        print("❌ No such date found!")
        return


    print(f"\nHabit details on {valid_date}:")

    pprint(content[valid_date])

    choice = input("Enter:\n1 to edit a habit\n2 to delete a habit\n➡  ").strip()

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

                del content[valid_date]

            open_to_write(content)

            print("🗑 Habit deleted successfully!")

        else:
            print("❌ No such habit found!")

    else:
        print("❌ Invalid choice! Please enter 1 or 2.")




def completion_percent():
    '''Overall Completion Percentage'''

    content = loading()

    if not content:
        print("Nothing in habit tracker file.")
        return

    total = sum(len(day) for day in content.values())

    complete = sum(val for day in content.values() for val in day.values())

    print(f"✅ Completion: {(complete / total) * 100:.2f}%" if total else "No habits to calculate.")





def progress_bar():
    '''Visual representation of progress'''

    content = loading()

    if not content:
        print("Nothing in habit tracker file.")
        return
    

    try:
        year = int(input("Enter Year: "))

        month = int(input("Enter Month (1-12): "))

        if not (1 <= month <= 12):
            raise ValueError
        
    except ValueError:
        print("❌ Invalid year or month!")
        return

    days_in_month = calendar.monthrange(year, month)[1]
    bar = []
    complete = 0

    for habit_date in content:

        try:
            d = datetime.strptime(habit_date, "%Y-%m-%d")

            if d.year == year and d.month == month:

                completed = all(content[habit_date].values())

                bar.append("\u2588" if completed else "\u2591")

                if completed:
                    complete += 1

        except ValueError:
            continue

    percent = f"{(complete / days_in_month) * 100:.2f}%"

    print("Progress: " + "".join(bar) + f" {percent}")





def opening_app():
    '''Opens App'''

    content = loading()

    today = date.today().isoformat()

    if today not in content:
        print("📝 You haven't added any habit today!")


    while True:
        print("\nChoose an option:")
        print("1. Add habit")
        print("2. Mark habit")
        print("3. View Calendar")
        print("4. Edit or delete habit")
        print("5. Progress Bar")
        print("6. Overall Completion Percentage")
        print("7. Exit")

        ask_user = input("➡  ").strip()

        if ask_user == "1":
            add_habit()
        elif ask_user == "2":
            marking_habit()
        elif ask_user == "3":
            view_calendar()
        elif ask_user == "4":
            edit_or_delete()
        elif ask_user == "5":
            progress_bar()
        elif ask_user == "6":
            completion_percent()
        elif ask_user == "7":
            print("👋 Thanks for using the Habit Tracker!")
            break
        else:
            print("❌ Please enter a valid option from 1 to 7.")
