def find_lcm(num1, num2):
    # Find the greater number among num1 and num2
    greater = max(num1, num2)

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1

    return lcm

# Example usage:
num1 = 12
num2 = 18

lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
