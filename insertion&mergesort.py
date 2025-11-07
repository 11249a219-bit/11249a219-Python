AIM:
To write a python program to implement insertion sort and merge sort using lists.
ALGORITHM FOR INSERTION SORT
1. Start
2. Input the list of elements
3. Loop from index 1 to end of the list:
o Store the current value in a variable key
o Set j = i - 1
o While j >= 0 and list[j] > key:
 Move list[j] to position j + 1
 Decrease j by 1
o Place key at position j + 1
4. Display the sorted list
5. Stop
ALGORITHM FOR MERGE SORT
1. Start
2. If the list has more than 1 element:
o Find the middle index
o Split the list into left and right halves
o Recursively call merge sort on both halves
o Merge the two sorted halves into a single sorted list
3. Use a helper function merge() to combine two sorted lists
4. Display the sorted list
5. Stop
PROGRAM FOR INSERTION SORT:
def insertion_sort(arr):
for i in range(1, len(arr)):
key = arr[i]
j = i - 1
while j >= 0 and arr[j] > key:
arr[j + 1] = arr[j]
j -= 1
arr[j + 1] = key
# Sample input
arr = [34, 8, 64, 51, 32, 21]
print("Original list:", arr)
insertion_sort(arr)
print("Sorted list (Insertion Sort):", arr)
PROGRAM FOR MERGE SORT:
def merge_sort(arr):
if len(arr) > 1:
mid = len(arr) // 2
left_half = arr[:mid]
right_half = arr[mid:]
merge_sort(left_half)
merge_sort(right_half)
i = j = k = 0
# Merge the sorted halves
while i < len(left_half) and j < len(right_half):
if left_half[i] < right_half[j]:
arr[k] = left_half[i]
i += 1
else:
arr[k] = right_half[j]
j += 1
k += 1
# Check for remaining elements
while i < len(left_half):
arr[k] = left_half[i]
i += 1
k += 1
while j < len(right_half):
arr[k] = right_half[j]
j += 1
k += 1
# Sample input
arr = [34, 8, 64, 51, 32, 21]
print("Original list:", arr)
merge_sort(arr)
print("Sorted list (Merge Sort):", arr)
OUTPUT:
Original list: [34, 8, 64, 51, 32, 21]
Sorted list (Insertion Sort): [8, 21, 32, 34, 51, 64]
Original list: [34, 8, 64, 51, 32, 21]
Sorted list (Merge Sort): [8, 21, 32, 34,
