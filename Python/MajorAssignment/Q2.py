# Q2
# Write two functions, hex2int and int2hex, that convert between hexadecimal digits (0, 1, 2, 3, 4, 5,
# 6, 7, 8, 9, A, B, C, D, E and F) and decimal (base 10) integers. The hex2int function is responsible
# for converting a string containing a single hexadecimal digit to a base 10 integer, while the int2hex
# function is responsible for converting an integer between 0 and 15 to a single hexadecimal digit. Each
# function will take the value to convert as its only parameter and return the converted value as its only
# result. Ensure that the hex2int function works correctly for both uppercase and lowercase letters.
# Your functions should display a meaningful error message and end the program if the parameter’s
# value is outside of the expected range.

def hex2int(hex_digit):
    try:
        return int(hex_digit, 16)
    except ValueError:
        print("Error: Invalid hexadecimal digit. It should be between 0 and F.")
        exit(1)

def int2hex(decimal_integer):
    try:
        return hex(decimal_integer)[2:].upper()
    except TypeError:
        print("Error: Invalid decimal integer. It should be between 0 and 15.")
        exit(1)

def main():
    # Test the hex2int function
    print(hex2int('A')) # Output: 10
    print(hex2int('1')) # Output: 1
    print(hex2int('F')) # Output: 15

    # Test the int2hex function
    print(int2hex(10)) # Output: A
    print(int2hex(1)) # Output: 1
    print(int2hex(15)) # Output: F

if __name__ == "__main__":
    main()


# OUTPUT:

# 10
# 1
# 15
# A
# 1
# F