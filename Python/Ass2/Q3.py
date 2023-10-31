# Take input from the user for the month's name and year
month = input("Enter the month's name: ").lower()
if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    days = 31
elif month == "april" or month == "june" or month == "september" or month == "november":
    days = 30
elif month == "february":
    days = "28 or 29 days"

# Display the number of days or a special message for February
if days is not None:
    print(f"{month.capitalize()} has {days} days.")
else:
    print("Invalid month name. Please enter a valid month name.")
