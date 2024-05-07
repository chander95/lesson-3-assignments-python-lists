# 2. Advanced List Methods and Identity Operators
# Objective:
# The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

#Task 1: Given the two lists:Find out which students both submitted their assignments and attended the class.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
both = []
for i in attended:
    #both = []
    if i in submitted:
        both.append(i)

print(str(both) + " all attended class and submitted their work on time!")


#Task 2: Check if the two lists are identical in terms of their content, regardless of order.
if attended not in submitted:
    print("These lists are not the same")

#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
removed = []
for i in attended:
    if i not in submitted:
        removed.append(i)

print(str(removed) + " were removed from the attended list.")