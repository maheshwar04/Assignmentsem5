# Prompt the user to enter a sound level in decibels
user_input = float(input("Enter a sound level in decibels: "))

if user_input < 40:
    print("This sound level is quieter than a Quiet Room.")
elif user_input == 40:
    print("This sound level is equivalent to a Quiet Room.")
elif user_input < 70:
    print("This sound level is between Quiet Room and Alarm Clock.")
elif user_input == 70:
    print("This sound level is equivalent to an Alarm Clock.")
elif user_input < 106:
    print("This sound level is between Alarm Clock and Gas Lawnmower.")
elif user_input == 106:
    print("This sound level is equivalent to a Gas Lawnmower.")
else:
    print("This sound level is louder than a Gas Lawnmower.")
