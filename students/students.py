# Here we are sorting out the lines in the file which is just english
'''
with open("students.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
'''

# But if we want to sort out by the student's name:
# 1st way where we will use a Python feature:
# Python allows you to pass functions as arguments into other functions.

students = []           #empty list

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}        #dictionary with "name" as key and "house" as value
        students.append(student)            #appending one student at a time as a dictionary in the students list

def get_name(student):
  return student['name']

def get_house(student):
   return student['house']

# Using above Python feature, we can pass get_name function as argument to below sorted function as key
for student in sorted(students, key=get_house):
  print(f"{student['name']} is in {student['house']}")
