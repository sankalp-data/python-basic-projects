import json
import datetime
filepath = r"Habit Tracker\habit_tracker_file.json"

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
        return [] # If file does not exist.
    except json.JSONDecodeError:
        return [] # If file does not contain anything or If file is corrupted
    
def add_habit():
    '''Adding new habit(s)'''
    content = loading()

    how_many_habits = int(input("How many habits you want to add?\n➡️ "))

    for _ in range(how_many_habits):
        date = input("Date (YYYY-MM-DD): ").strip()
        habit = input("Habit: ").strip()

        # Check if date already exists
        if date in content:
            if habit not in content[date]:
                content[date].append(habit)  # Append to existing list
        else:
            content[date] = [habit]  # Create new list with habit

    open_to_write(content)
    print("✅ Habits saved successfully!")





