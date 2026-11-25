# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(is_even(num))

# Write a function largest(a, b) that returns the larger number.

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(10, 20))

# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(10)

# Write a function sum_n(n) that returns the sum of numbers from 1 to n.

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_n(10))

# Write a function table(n) that prints the multiplication table of n from 1 to 10.

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5)

# Write a function that takes a list and returns how many even numbers it contains.

def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6]))

# Without using max(), write a function that returns the largest number in a list.

def find_max(numbers):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest

print(find_max([10, 25, 5, 40, 15]))

# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()

# Write a function that returns True if a string is a palindrome.

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(palindrome("madam"))

# Write a function that counts the vowels in a string.

def count_vowels(s):
    count = 0
    for i in s:
        if i.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))

# Write a function that returns the second largest number in a list without using sort().

def second_largest(numbers):
    largest = second = float('-inf')

    for i in numbers:
        if i > largest:
            second = largest
            largest = i
        elif largest > i > second:
            second = i

    return second

print(second_largest([10, 20, 30, 40, 50]))

# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Correct Guess!")
            break
        elif guess < number:
            print("Too Low! Try Again.")
        else:
            print("Too High! Try Again.")

guessing_game()

# Write a function grade(marks) that returns a grade based on marks.
# A for marks >= 90
# B for marks >= 80
# C for marks >= 70
# D for marks >= 60
# Otherwise F

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


marks = int(input("Enter your marks: "))
print("Grade:", grade(marks))

