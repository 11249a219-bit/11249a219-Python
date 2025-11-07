AIM:
To write a python program to find the best of two test average marks out of three test’s
marks accepted from the user.

ALGORITHM:
Step 1: Start
Step 2: Input three test marks: test1, test2, test3
Step 3: Store the three test marks in a list or array called marks
Step 4: Sort the marks list in descending order
Step 5: Select the first two values from the sorted list as best_two
Step 6: Calculate the average:
average = (best_two[0] + best_two[1]) / 2
Step 7: Display the best two marks
Step 8: Display the calculated average
Step 9: Stop
PROGRAM:
# Accept three test marks from the user
test1 = float(input("Enter marks for Test 1: "))
test2 = float(input("Enter marks for Test 2: "))
test3 = float(input("Enter marks for Test 3: "))

# Store the marks in a list
marks = [test1, test2, test3]

# Sort the list in descending order
marks.sort(reverse=True)

# Calculate the average of the best two marks
best_two_avg = (marks[0] + marks[1]) / 2
# Display the result
print("The best two test marks are:", marks[0], "and", marks[1])
print("The average of the best two test marks is:", best_two_avg)
OUTPUT:
Enter marks for Test 1: 72
Enter marks for Test 2: 85
Enter marks for Test 3: 68
Best two test marks are: [85.0, 72.0]
Average of best two test marks is: 78.5
