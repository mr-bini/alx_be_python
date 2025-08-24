# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unknown priority level"

if time_bound == "yes":
    print(f"Reminder: {base} that requires immediate attention today!")
else:
    print(f"Reminder: {base}. Consider completing it when you have free time.")
