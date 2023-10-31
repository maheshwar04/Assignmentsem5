def are_coprime(num1, num2):
    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd = find_gcd(num1, num2)
    return gcd == 1

# Example usage:
num1 = 21
num2 = 8

if are_coprime(num1, num2):
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are not coprime.")

# op : 21 and 8 are coprime.