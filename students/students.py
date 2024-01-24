# Here we are sorting out the lines in the file which is just English
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
        students.append(student)            #appending one student at a time as a dictionary in the students' list


# Created solely for returning the value of the key name which is called by the sorted function to sort
def get_name(student):
  return student['name']


# Created solely for returning the value of the key house which is called by the sorted function to sort
def get_house(student):
   return student['house']

# Using the above Python feature, we can pass get_name function as an argument to the below sorted function as the key
for student in sorted(students, key=get_name):
  print(f"{student['name']} is in {student['house']}")
