total = 0
count = 0

value = float(input("Enter a value (0 to quit): "))

if value == 0:
    print("Error: The first value cannot be 0.")
else:
    while value != 0:
        total += value
        count += 1
        value = float(input("Enter a value (0 to quit): "))

    if count > 0:
        average = total / count
        print(f"The average of the entered values is: {average}")
    else:
        print("No values entered.")
#op        
# Enter a value (0 to quit): 56
#Enter a value (0 to quit): 54
#Enter a value (0 to quit): 0
#The average of the entered values is: 55.0