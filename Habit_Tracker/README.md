#  Habit Tracker (Python CLI App)

A simple yet powerful console-based Habit Tracker built in Python to help you build and maintain daily habits.

It stores habit progress date-wise in a JSON file and gives you a visual overview of your progress through a calendar view and progress bar.

📌 **Features:**

 - Add one or more habits for today
 - Mark habits as completed
 - View calendar with ✅ or ❌ for each day
 - Edit or delete specific habits
 - See overall completion percentage
 - View visual progress bar for a month
 - Stores data in a readable JSON format
 - Fully works offline



📁 **Data Format (JSON):**
```json
{
  "2025-07-21": ["Workout", "Read"],
  "2025-07-22": ["Meditate"]
} 
```


# Functions Used

 - add_habit():
   Prompts for a date and adds one or more habits under that date.

 - marking_habit():
   Marks any habit for a selected date as completed (True).

 - loading():
   Loads habit data from JSON, handles missing/corrupt files.

 - open_to_write():
   Writes updated data safely into the JSON file.
  
 - view_calendar():
   Displays habit status day-by-day inside a calendar layout.

 - edit_or_delete():
  Edit a habit name for a given date.
  Delete all habits for a date.

 - progress_bar():
  Graphical progress for a selected month.

 - completion_percent():
  Displays overall habit completion rate.



# Developer Notes

 - The view_calendar() function was the most challenging part and was built with some help to handle alignment and date logic correctly using the calendar module.

 - All other logic was written by me as part of my learning journey.

 - I plan to increase the readability and modularity of the code in future updates.


# How to Run

1. Install Python
  - Make sure Python 3.6 or higher is installed.

2. Download or Clone Your Project Folder
  - git clone https://github.com/sankalp-data/habit-tracker.git
    cd habit-tracker
  
3. Run the Python Script
  - python habit_tracker.py


