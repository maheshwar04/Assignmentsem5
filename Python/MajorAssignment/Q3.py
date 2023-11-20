# Q3
# (Arbitrary Base Conversions) Write a program that allows the user to convert a number from one
# base to another. Your program should support bases between 2 and 16 for both the input number
# and the result number. If the user chooses a base outside of this range then an appropriate error
# message should be displayed and the program should exit. Divide your program into several functions,
# including a function that converts from an arbitrary base to base 10, a function that converts from base
# 10 to an arbitrary base, and a main program that reads the bases and input number from the user.

def int_to_base(num, base):
    convert_string = "0123456789ABCDEF"
    if num < base:
        return convert_string[num]
    else:
        return int_to_base(num // base, base) + convert_string[num % base]

def base_to_int(num, base):
    convert_string = "0123456789ABCDEF"
    num = num[::-1]
    result = 0
    for i in range(len(num)):
        result += convert_string.index(num[i]) * (base ** i)
    return result

def main():
    base_in = int(input("Enter base of input number (between 2 and 16): "))
    base_out = int(input("Enter base for output number (between 2 and 16): "))
    if not (2 <= base_in <= 16) or not (2 <= base_out <= 16):
        print("Error: Base must be between 2 and 16")
        return
    num = input("Enter the number to convert: ")
    base10 = base_to_int(num, base_in)
    print("Number in base 10:", base10)
    print("Number in base", base_out, ":", int_to_base(base10, base_out))

main()


# OUTPUT:

# Enter base of input number (between 2 and 16): 2
# Enter base for output number (between 2 and 16): 16
# Enter the number to convert: 1011
# Number in base 10: 11
# Number in base 16 : B