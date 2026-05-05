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

def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse


def fibonacci(n):
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


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
        
strings = ["radar", "hello", "level", "world", "madam", "python"]
print("\nChecking if strings are palindromes:") 
for s in strings:
    if is_palindrome(s):
        print(f'"{s}" is a palindrome')
    else:
        print(f'"{s}" is not a palindrome')
print("\nFibonacci sequence (first 10 numbers):")
print(fibonacci(10))
# for number in numbers:
#     result = check_even_odd(number)
#     print(f"{number} is {result}")