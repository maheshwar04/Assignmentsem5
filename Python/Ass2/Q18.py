def multiply_by_repeated_addition(num1, num2):
    result = 0

    for _ in range(num2):
        result += num1

    return result

# Example usage:
num1 = 7
num2 = 5

result = multiply_by_repeated_addition(num1, num2)
print(f"{num1} * {num2} = {result}")

#op : 7 * 5 = 35