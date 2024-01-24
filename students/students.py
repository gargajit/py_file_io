# Here we are sorting out the lines in the file which is just English
'''
with open("students.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
'''

# But if we want to sort out by the student's name:
# 1st way where we will use a Python feature:
# PYTHON FEATURE: Python allows you to pass functions as arguments into other functions.

students = []           #empty list

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}        #dictionary with "name" as key and "house" as value
        students.append(student)                        #appending one student at a time as a dictionary in the students' list


# Temp function: Created solely for returning the value of the key name which is called by the sorted function to sort
def get_name(student):
  return student['name']


# Temp function: Created solely for returning the value of the key house which is called by the sorted function to sort
def get_house(student):
   return student['house']

# Using the above Python feature, we can pass get_name function as an argument to the below sorted function as the key
# Here notice that the get_name or get_house if written is not called using parenthesis
# but passed only as the name so that the sorted function can call that sorted function for the user.
'''
for student in sorted(students, key=get_name):
  print(f"{student['name']} is in {student['house']}")
'''


'''
If you are defining something and immediately using it but never, once again, need the name of that function, 
like get_name or get_house, we can further tighten the above code.

Get rid of the function we defined, and in sorted function, instead of passing `key`, the name of a function, 
we can pass the key to what is called the `lambda` function.

`lambda` is an anonymous function.
'''
  
for student in sorted(students, key=lambda student: student['name']):
  print(f"{student['name']} is in {student['house']}")
