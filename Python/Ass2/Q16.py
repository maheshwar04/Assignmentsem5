def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    return digit_sum == number

# Find and print Armstrong numbers in the range from 1 to 1000
for num in range(1, 1001):
    if is_armstrong_number(num):
        print(num ,end =" ")
 
# 1 2 3 4 5 6 7 8 9 153 370 371 407 