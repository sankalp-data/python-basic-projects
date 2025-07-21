# 🧠 Habit Tracker (In Progress)

This is a simple console-based Habit Tracker written in Python.  
It allows you to track daily habits by storing them based on date into a JSON file.

📌 **Current Features:**
- Add one or more habits for a given date
- Save habits in a JSON file
- Prevents overwriting habits for the same day

🔧 **Upcoming Features (Planned):**
- View all habits by date
- Delete or update existing habits
- Track weekly progress
- Visual summary using charts (e.g., matplotlib or plotly)

📁 **Data Format (JSON):**
```json
{
  "2025-07-21": ["Workout", "Read"],
  "2025-07-22": ["Meditate"]
}
