def sum_of_digits(number):
    digit_sum = 0
    num_str = str(number)

    for digit in num_str:
        digit_sum += int(digit)

    return digit_sum

# Example usage:
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of the digits of {num} is: {result}")

# The sum of the digits of 67 is: 13