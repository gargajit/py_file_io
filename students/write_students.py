import csv

name = input("Enter Name: ").strip()
address = input("Enter Address: ").strip()

'''
# With csv.writer, the onus is on us to pass in a list of all of the values
# that we want to put from left to write 
with open("write_students.csv", mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, address])
'''

'''
With csv.Dictwriter, they could be in any order in the dictionary 
so even if we change the writerow order, but it is a dictionary
so the ordering in this case does not matter so long as the key is there and value is there.
And because I have passed the fieldnames as the second argument to DictWriter, it ensures
that the library knows exactly which column contains name or address, respectively.
'''
with open("write_students.csv", mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "address"])
    # fieldnames is a way to help Dictionary to know the order in which those columns are, when writing it out
    writer.writerow({"name": name, "address": address})
