import csv

students = []

with open("students_address.csv") as file:
    reader = csv.reader(file)
    # One Way
    '''
    for row in reader:
        student = {"name": row[0], "home": row[2]}
        students.append(student)
    '''
    # Second Way
    '''
    for row in reader:
        students.append({"name": row[0], "home": row[2]})
    '''
    #Third Way
    for name, home in reader:
        students.append({"name": name, "home": home})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
        
