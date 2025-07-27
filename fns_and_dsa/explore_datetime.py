from datetime import datetime
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date
def calculate_future_date(days):
    future_date = display_current_datetime() + datetime.timedelta(days=days)
    return future_date.strftime("%Y-%m-%d %H:%M:%S")


print(f"Current date and time: {display_current_datetime()}")
days = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date(days)}")