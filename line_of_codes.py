import sys

counter = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith('.py'):
    sys.exit("Not a Python file")

try:
    with open(f"{sys.argv[1]}") as file:
        for line in file:
            s = line.lstrip()
            if s.startswith('#'):
                continue
            if len(line.strip()) == 0:
                continue
            else:
                counter += 1
    print(counter)

except FileNotFoundError:
    print("File does not exit")
