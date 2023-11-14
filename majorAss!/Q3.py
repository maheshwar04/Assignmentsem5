def convert_to_decimal(number, base):
    try:
        decimal_value = int(str(number), base)
        return decimal_value
    except ValueError:
        print("Error: Invalid input for the specified base.")
        exit()

def convert_from_decimal(decimal_value, target_base):
    try:
        result = format(decimal_value, f"0{target_base}X")
        return result
    except ValueError:
        print("Error: Unable to convert to the specified base.")
        exit()

def main():
    input_base = int(input("Enter the base of the input number (between 2 and 16): "))
    if not (2 <= input_base <= 16):
        print("Error: Input base must be between 2 and 16.")
        exit()

    input_number = input(f"Enter a number in base {input_base}: ")

    target_base = int(input("Enter the target base (between 2 and 16): "))
    if not (2 <= target_base <= 16):
        print("Error: Target base must be between 2 and 16.")
        exit()

    decimal_value = convert_to_decimal(input_number, input_base)

    result = convert_from_decimal(decimal_value, target_base)

    print(f"The equivalent of {input_number} in base {target_base} is: {result}")

if __name__ == "__main__":
    main()
