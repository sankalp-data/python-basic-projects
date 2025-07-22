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