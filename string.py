AIM:
To write a Python program to find the string similarity between two given strings.
ALGORITHM:
1. Start
2. Input two strings: string1 and string2
3. Find the length of the shorter string → min_len
4. Initialize a counter match_count = 0
5. Loop from i = 0 to min_len - 1:
A. If string1[i] == string2[i] → increment match_count
6. Calculate similarity ratio:
B. similarity = (match_count / max(len(string1), len(string2))) * 100
7. Display the similarity percentage
8. Stop
PROGRAM:
# Input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Find length of shorter string
min_len = min(len(string1), len(string2))
max_len = max(len(string1), len(string2))
# Initialize match counter
match_count = 0
# Compare characters
for i in range(min_len):
if string1[i] == string2[i]:
match_count += 1
#Calculate similarity percentage
similarity = (match_count / max_len) * 100
# Output
print(f"String similarity: {similarity:.2f}%")
OUTPUT:
Enter the first string: apple
Enter the second string: apply
String similarity: 80.00%
Enter the first string: hello
Enter the second string: yellow
String similarity: 60.00%
