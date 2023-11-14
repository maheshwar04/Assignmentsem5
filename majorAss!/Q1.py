def binary_to_decimal(binary_str):
    decimal_num = 0
    binary_str = binary_str[::-1]

    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decimal_num += 2**i

    return decimal_num

def main():
    binary_input = input("Enter a binary number: ")

    if not set(binary_input).issubset({'0', '1'}):
        print("Invalid binary number. Please enter a valid binary number.")
        return

    decimal_result = binary_to_decimal(binary_input)

    print(f"The decimal equivalent of {binary_input} is: {decimal_result}")

if __name__ == "__main__":
    main()
