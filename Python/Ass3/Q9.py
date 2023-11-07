def find_maximum_of_three(num1, num2, num3):
    def find_maximum(a, b):
        if a > b:
            return a
        else:
            return b

    max_of_first_two = find_maximum(num1, num2)
    overall_max = find_maximum(max_of_first_two, num3)

    return overall_max

# Example usage:
num1 = 10
num2 = 25
num3 = 15

maximum = find_maximum_of_three(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {maximum}")
