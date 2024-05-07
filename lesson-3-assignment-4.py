# 4. Deep Dive into Python Lists
# Objective:
# The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

# Problem Statement:
# You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists: 
#Filter out students who have grades below 80. Print the name, grade and activiy. 
#Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

below_80 = []
total_list = []
total_list.append(students)
total_list.append(grades)
total_list.append(activities)
#print(total_list)
#print(total_list[1][0])

for i in range(len(grades)):
    if grades[i] < 80:
        index = i
        below_80.append(total_list[0][i] + ", " + str(total_list[1][i]) +  ", " + total_list[2][i])
        print(below_80)