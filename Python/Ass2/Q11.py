def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

# Example usage:
num1 = 48
num2 = 18

gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")
