def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_factors(number):
    factors = []
    divisor = 2

    while number > 1:
        if number % divisor == 0 and is_prime(divisor):
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors

n = int(input("Enter an integer (2 or greater): "))

if n < 2:
    print("Error: Please enter an integer greater than or equal to 2.")
else:
    factors = prime_factors(n)
    
    print(f"The prime factors of {n} are:")
    for factor in factors:
        print(factor,end=" ")

#op : Enter an integer (2 or greater): 54
#The prime factors of 54 are:
#2 3 3 3 