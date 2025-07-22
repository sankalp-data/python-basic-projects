import json
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
            print(content[date])
            ask  = (input("Which habit you want to mark as True i.e. Completed? \n ➡️ "))
            content[date][ask] = True
        
        else:
            print("No such date...")
            return

    else:
        print("Nothing in habit_tracker file")

    open_to_write(content)        
            


# add_habit()
marking_habit()







