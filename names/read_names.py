# 1st way: Here we are creating a list by reading all the lines and then using for loop printing each name
'''
with open("name.txt", "r") as file:         
    lines = file.readlines()        #lines is a list

#print(type(lines))
for line in lines:
    #print("hello,", line)
    # the output is one additional newline which is due to the '/n' we added while writing the name.txt
    # 1 way to modify default value og endline for print
    #print("hello,", line, end="")
    # 2nd way is to strip the right of the line whitespaces by using 'lstrip()' function
    print("hello,", line.rstrip())
'''



# 2nd way: Here instead of reading all lines, we are taking one line and printing it immediately and then moving to next line
'''
with open("name.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
'''


# But we can sort the names in the text file using 2nd way. 
# So, if you want to print names in a sorted manner, without affecting the text file we have combine things:

names = []

with open("name.txt") as file:
    for line in file:
        names.append(line.rstrip())

# A to Z order
for name in sorted(names):
    print(f"Hello, {name}")
'''
# Z to A order (reverse)
for name in sorted(names, reverse=True):
    print(f"Hello, {name}")
'''




'''
# OR we can make it compact by looping line on the sorted file

with open("name.txt") as file:
    for line in sorted(file): 
        print(f"Hello,", line.rstrip())
'''
