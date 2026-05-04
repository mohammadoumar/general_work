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


# Examples
print("\nChecking if numbers are even or odd:")
numbers = [1, 2, 3, 4, 5, 10, 15, 20, 42, 99]
for number in numbers:
    result = check_even_odd(number)
    print(f"{number} is {result}")