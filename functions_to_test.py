# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    result = a + b
    return result

def find_maximum(a, b, c):
    return max(a, b, c)

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    

def count_word_occurrences(text, word):
    pass


def read_file_lines(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return lines

def factorial(n):
    if n <= 0:
        raise ValueError("Factorial is not defined for negative numbers.")
        return ""
    if n == str(n):
        raise TypeError("Input must be an integer.")
    else:
        return n * factorial(n - 1)

def is_prime(n):
    if n < 0:
        raise ValueError("Prime is not defined for negative numbers.")
    if n == str(n):
        raise TypeError("Input must be an integer.")
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sort_numbers(numbers):
    for i in numbers:
        if i == str(i):
            raise TypeError("Input must be an integer.")
    if numbers == []:
        return []
    else:
        return sorted(numbers)

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == str(n):
        raise TypeError("Input must be an integer.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def tower_of_hanoi(n, source, auxiliary, target):
    
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        if Person.name == int(Person.name) or Person.age == str(Person.age):
            raise TypeError("Name must be  a string and age must be an integer.")

if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g