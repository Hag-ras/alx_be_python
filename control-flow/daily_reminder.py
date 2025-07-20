task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop to ensure valid priority input
while priority not in ['high', 'medium', 'low']:
    print("Invalid input. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Match-case for priority handling
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"

# Conditional for time sensitivity
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Final output
print("\nReminder:", reminder)
