# 🧠 Habit Tracker (In Progress)

This is a simple console-based Habit Tracker written in Python.  
It allows you to track daily habits by storing them based on date into a JSON file.

📌 **Features:**
- Add one or more habits for a given date
- Save habits in a JSON file
- Prevents overwriting habits for the same day

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


# About View Calendar Function
The view_calendar() function — which displays habit status day-by-day inside a calendar layout — was the most challenging part. I took help (from ChatGPT) specifically to understand how to:

 - Use the calendar module to build a month view

 - Format the day layout correctly

 - Match date strings from JSON with the calendar

Every other part of the project (like adding habits, marking them, file handling, data structures, etc.) was coded fully by me from scratch.


