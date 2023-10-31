# Input the age in human years
human_age = float(input("Enter the age in human years: "))

# Check for negative input
if human_age < 0:
    print("Error: Please enter a non-negative number.")
else:
    # Calculate dog years
    if human_age <= 2:
        dog_years = 10.5 * human_age
    else:
        dog_years = 21 + 4 * (human_age - 2)

    # Display the result
    print(f"{human_age} human years is equivalent to {dog_years} dog years.")

#op : 24.0 human years is equivalent to 109.0 dog years.