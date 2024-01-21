'''
name = input("Enter the name: ")
file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()
# here we have closed the file using the above function. This is a manual way
'''

# This is more pythonic way. Now we will use "with" that will indicate to automatically open the name.txt and also close it.
name = input("Enter the name: ")

with open("name.txt", "a") as file:
    file.write(f"{name}\n")
