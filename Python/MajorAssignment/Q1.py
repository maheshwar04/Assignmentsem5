# Q1
# Write a program that converts a binary (base 2) number to a decimal (base 10). Your program should
# begin by reading the binary number from the user as a string. Then, it should compute the equivalent
# decimal number by processing each digit in the binary number. Finally, your program should display
# the equivalent decimal number with an appropriate message.

def binary_to_decimal(binary):
    binary = binary.strip()
    decimal = 0
    power = 0

    for digit in binary[::-1]:
        if digit != '0' and digit != '1':
            print("Error: Invalid binary digit.")
            exit(1)
        decimal += int(digit) * (2**power)   
        power += 1
    
    return decimal

binary = input("Enter a binary number: ")
decimal = binary_to_decimal(binary)
print(f"The decimal equivalent is {decimal}.")


# OUTPUT:

# Enter a binary number: 1110
# The decimal equivalent is 14.