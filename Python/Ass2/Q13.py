# def calculate_series_sum(x, n):
#     series_sum = 0
#     factorial = 1  # Initialize the factorial as 1
#     for i in range(n):
#         if i % 2 == 0:
#             term = x ** (2 * i) / factorial
#         else:
#             term = -x ** (2 * i) / factorial
#         series_sum += term

#         # Update the factorial for the next term
#         factorial *= (2 * i + 1) * (2 * i + 2)

#     return series_sum

# # Example usage:
# x = 2  # Replace with your desired value of x
# n = 5  # Replace with the number of terms you want in the series
# result = calculate_series_sum(x, n)
# print(f"The sum of the first {n} terms of the series for x = {x} is approximately {result:.4f}")


import math

def calculate_exponential_series(x, n_terms):
    result = 1  # The first term (n = 0)
    term = 1
    for n in range(1, n_terms):
        term *= x / n  # Calculate the next term based on the previous one
        result += term
    return result

x = 2.0  # You can change this value to any desired value of x
n_terms = 5  # You can change this to the number of terms you want in the series

approximation = calculate_exponential_series(x, n_terms)
actual_result = math.exp(x)

print(f"Approximation of e^{x} with {n_terms} terms: {approximation}")
print(f"Actual result of e^{x}: {actual_result}")

