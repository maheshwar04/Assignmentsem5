def is_perfect_number(n):
    if n <= 0:
        return False  # Perfect numbers are positive integers only

    divisors_sum = 1  # Initialize with 1 as 1 is always a divisor

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i

    return divisors_sum == n

# Example usage:
number=int(input("Enter the number : "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
