import os

cwd = os.getcwd()
current_dir = cwd.split("\\")[-1]

print("Current directory: " + current_dir)


def check_even_odd(num):
    """Check if a number is even or odd."""
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Examples
print("\nChecking if numbers are even or odd:")
numbers = [1, 2, 3, 4, 5, 10, 15, 20, 42, 99]
for number in numbers:
    result = check_even_odd(number)
    print(f"{number} is {result}")

print("\nChecking if numbers are prime:")
for number in numbers:
    if is_prime(number):
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")
# for number in numbers:
#     result = check_even_odd(number)
#     print(f"{number} is {result}")