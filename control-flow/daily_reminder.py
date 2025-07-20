task = input('Enter your task: ')
priority = input('Priority (high/medium/low): ')
time = input('Is it time-bound? (yes/no): ')
message =''
match priority:
    case 'high':
        message += f"'{task}' is a {priority} priority"
    case 'medium':
        message += f"'{task}' is a {priority} priority"
    case 'low':
        message += f"'{task}' is a {priority} priority"
    case _:
        print('invalid priority input')
match time:
    case 'yes':
        message += f' that requires immediate attention today!'
    case 'no':
        message += f'. Consider completing it when you have free time.'
    case _:
        print('invalid time input')
print(message)