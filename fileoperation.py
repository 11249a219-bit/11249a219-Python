AIM:
To write a python program to accept a file name from the user and perform the following
operations 1. Display the first N line of the file 2. Find the frequency of occurrence of the word
accepted from the user in the file.
ALGORITHM:
1. Start
2. Accept the filename from the user.
3. Open the file in read mode.
4. Ask the user to input number of lines (N) to display.
5. Read and display the first N lines.
6. Ask the user to enter a word to search.
7. Read the entire file again.
8. Convert content and word to lowercase.
9. Use .count() to find the number of occurrences of the word.
10. Display the frequency.
11. Close the file.
12. End
PROGRAM:
def main():
# Step 1: Input file name
filename = input("Enter the filename: ")
# Step 2: Open file and display first N lines
file = open(filename, 'r')
N = int(input("Enter number of lines to display: "))
print(f"\nFirst {N} lines of the file:")
for i in range(N):
line = file.readline()
if line == '':
print("End of file reached.")
break
print(line.strip())
file.close()
# Step 3: Count word frequency
word = input("\nEnter the word to find its frequency: ").lower()
file = open(filename, 'r')
content = file.read().lower()
frequency = content.count(word)
file.close()
print(f"\nThe word '{word}' occurred {frequency} times in the file.")
# Run the function
main()
OUTPUT:
Enter the filename: demo.txt
Enter number of lines to display: 2
Enter the word to find its frequency: data
First 2 lines of the file:
Data is essential in today’s world.
Big data is changing the industry.
The word 'data' occurred 2 times in the file
