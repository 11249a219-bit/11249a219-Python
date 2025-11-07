AIM:
To develop a Python program to check whether a given number is palindrome or not and
also count the number of occurrences of each digit in the input number.
ALGORITHM
1. Start
2. Input the number as a string (num).
3. Check for Palindrome:
a. Reverse the string using slicing (num[::-1]).
b. Compare the reversed string with the original:
i. If equal → Print that the number is a palindrome.
ii. Else → Print that the number is not a palindrome.
4. Initialize an empty dictionary digit_count.
5. For each character digit in the input string num:
a. If the character is a digit:
i. If the digit exists in the dictionary, increment its count.
ii. Else, add it to the dictionary with count 1.
6. Display the digit occurrence count by iterating over the dictionary in sorted order of digits.
7. End
PROGRAM:
# Get input from the user
num = input("Enter a number: ")
# Check for palindrome
if num == num[::-1]:
print(f"{num} is a palindrome.")
else:
print(f"{num} is not a palindrome.")
# Count digit occurrences
digit_count = {}
for digit in num:
if digit.isdigit(): # Ensure only digits are considered
digit_count[digit] = digit_count.get(digit, 0) + 1
print("\nDigit Occurrence Count:")
for digit in sorted(digit_count):
print(f"Digit {digit} occurs {digit_count[digit]} time(s)")
OUTPUT:
Enter a number: 12321
12321 is a palindrome.
Digit Occurrence Count:
Digit 1 occurs 2 time(s)
Digit 2 occurs 2 time(s)
Digit 3 occurs 1 time(s)
