AIM:
Fibonacci sequence: Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program
which accepts a value for N (where N >0) as input and pass this value to the function. Display
suitable error message if the condition for input value is not followed.
ALGORITHM:
Step 1: Start
Step 2: Input value N from user
Step 3: Check if N is a digit and N > 0
 If not, print "Invalid input. Please enter a positive integer."
 Go to Step 8
Step 4: Convert N to integer
Step 5: Define a function fibonacci(n)
 Initialize a = 0, b = 1
 Loop n times:
 Print a
 Set a, b = b, a + b
Step 6: Call fibonacci(N)
Step 7: End function
Step 8: Stop
PROGRAM:
# Function to print Fibonacci sequence
def fibonacci(n):
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
print(a, end=' ')
a, b = b, a + b
# Get user input
N = input("Enter the number of terms (N > 0): ")
# Validate input
if N.isdigit():
N = int(N)
if N > 0:
fibonacci(N)
else:
print("Invalid input. Please enter a number greater than 0.")
else:
print("Invalid input. Please enter a positive integer.")
OUTPUT:
Enter the number of terms (N > 0): 6
Fibonacci sequence:
0 1 1 2 3 5
Enter the number of terms (N > 0): 0
Invalid input. Please enter a number greater than 0
