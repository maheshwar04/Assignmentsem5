def hex2int(hex_digit):
    try:
        decimal_value = int(hex_digit, 16)
        if 0 <= decimal_value <= 15:
            return decimal_value
        else:
            raise ValueError("Hexadecimal digit must be between 0 and 15.")
    except ValueError:
        print("Error: Invalid hexadecimal digit.")
        exit()

def int2hex(decimal_value):
    if 0 <= decimal_value <= 15:
        return hex(decimal_value)[2:].upper()
    else:
        print("Error: Decimal value must be between 0 and 15.")
        exit()

def main():
    # Test hex2int function
    hex_input = input("Enter a hexadecimal digit: ")
    decimal_result = hex2int(hex_input)
    print(f"The decimal equivalent of {hex_input} is: {decimal_result}")

    # Test int2hex function
    decimal_input = int(input("Enter a decimal value (0-15): "))
    hex_result = int2hex(decimal_input)
    print(f"The hexadecimal equivalent of {decimal_input} is: {hex_result}")

if __name__ == "__main__":
    main()
