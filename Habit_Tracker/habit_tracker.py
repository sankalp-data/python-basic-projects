import json
from pprint import pprint
import calendar
filepath = r"Habit_Tracker\habit_tracker_file.json"

def open_to_write(file):
    '''Open file for writing'''

    with open(filepath,"w") as f:
        json.dump(file,f,indent=4)



def loading():
    '''Load Data from habit_tracker_file.json'''

    try:
        with open(filepath,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {} # If file does not exist.
    except json.JSONDecodeError:
        return {} # If file does not contain anything or If file is corrupted
    
def add_habit():
    '''Adding new habit(s)'''
    content = loading()
    try:
        how_many_habits = int(input("How many habits you want to add?\n➡️   "))
    except ValueError:
        print("Please enter valid input!")
        return
    try:
        date = input("Date (YYYY-MM-DD): ").strip()
        
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD")
        return
    
    if date not in content:
        content[date] = {}
    
    for _ in range(how_many_habits):
        habit = input("Habit :- ").strip()
        if habit:
            content[date][habit] = False

    open_to_write(content)

    print("✅ Habits saved successfully!")

    
        
def marking_habit():
    '''Marking which habit is complete''' 
    content = loading()

    if content:
        try:
            date = input("Date :- ").strip()
        except ValueError:
            print("Invalid Input!!")
            return
        
        if date in content:
            pprint(content[date])
            ask  = (input("Which habit you want to mark as True i.e. Completed? \n ➡️ "))
            if ask in content[date]:
                content[date][ask] = True
            else:
                print("Habit not foumd!")
                return  

        else:
            print("No such date...")
            return

    else:
        print("Nothing in habit_tracker file")

    open_to_write(content)

            
            

def view_calendar():
    content = loading()

    try:
        year = int(input("Enter Year :- "))
        if year < 1 or year > 9999:
            print("❌ Please enter year between 1 and 9999")
            return

        month = int(input("Enter Month :- "))
        if month < 1 or month > 12:
            print("❌ Please enter valid month (1-12)")
            return

    except ValueError:
        print("❌ Please enter valid format or data type!")
        return

    # Get number of days in the month
    days_in_month = calendar.monthrange(year, month)[1]

    # Prepare calendar layout
    print("\n📅 Habit Tracker Calendar")
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")

    # Get the first weekday of the month (0 = Monday)
    start_day = calendar.monthrange(year, month)[0]
    day_counter = 1
    row = []

    # Fill the first week with blanks
    for _ in range(start_day):
        row.append("  ")

    while day_counter <= days_in_month:
        day_str = f"{day_counter:02}"
        full_date = f"{year}-{month:02}-{day_str}"

        if full_date in content:
            # Check if all habits are True
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

    # Print remaining days
    if row:
        print("  ".join(row))



