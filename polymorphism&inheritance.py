AIM:
To Write a python program to find the whether the given input is palindrome or not (for
both string and integer) using the concept of polymorphism and inheritance.
ALGORITHM:
1. Start
2. Define a base class called PalindromeChecker with a method is_palindrome(self, value).
3. Define two derived classes:
a) StringPalindromeChecker that overrides is_palindrome() to handle strings.
b) IntegerPalindromeChecker that overrides is_palindrome() to handle integers.
4. In the is_palindrome() method of each class:
a) Reverse the input (string or number) and compare it with the original.
5. Accept input from the user and determine whether it is an integer or string.
6. Create an object of the appropriate class.
7. Call the is_palindrome() method and display the result.
8. End
PROGRAM:
# Base class
class PalindromeChecker:
def is_palindrome(self, value):
raise NotImplementedError("Subclasses should implement this!")
# Derived class for string palindrome
class StringPalindromeChecker(PalindromeChecker):
def is_palindrome(self, value):
value = value.lower().replace(" ", "") # Normalize string
return value == value[::-1]
# Derived class for integer palindrome
class IntegerPalindromeChecker(PalindromeChecker):
def is_palindrome(self, value):
str_value = str(value)
return str_value == str_value[::-1]
# Main logic
input_value = input("Enter a value (string or integer): ")
if input_value.isdigit():
checker = IntegerPalindromeChecker()
is_pal = checker.is_palindrome(int(input_value))
else:
checker = StringPalindromeChecker()
is_pal = checker.is_palindrome(input_value)
# Display the result
if is_pal:
print("The input is a palindrome.")
else:
print("The input is not a palindrome.")
OUTPUT:
Enter a value (string or integer): 12321
The input is a palindrome.
Enter a value (string or integer): Racecar
The input is a palindrome.
Enter a value (string or integer): Hello
The input is not a palindrome
