import random

# Simulate a spin
spin_result = random.randint(0,37)
if spin_result== 37:
    spin_result=00

# Display the number selected
print(f"The spin resulted in {spin_result}...")

# Check and display the bets to be paid
if spin_result == 0 or spin_result == 00:
    print(f"Pay {spin_result}")
    print("Pay Green")
else:
    if (spin_result == 1 or spin_result == 3 or spin_result == 5 or spin_result == 7 
        or spin_result == 9 or spin_result == 12 or spin_result == 14 or   spin_result == 16 or   
        spin_result == 18 or  spin_result == 19 or    spin_result == 21 or   spin_result == 23 
        or spin_result == 25 or  spin_result == 27 or  spin_result == 30 or   
         spin_result == 32 or spin_result == 34 or  spin_result == 36):
        print(f"Pay {spin_result}")
        print("Pay Red")
        
    else:
        print(f"Pay {spin_result}")
        print("Pay Black")

    if spin_result % 2 == 0:
        if spin_result != 0:
            print("Pay Even")
    else:
        print("Pay Odd")

    if spin_result >= 1 and spin_result <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")

