my_file = open("names.txt")
for name in my_file.readlines():
    print(f"hello {name}", end='') # end is telling what to print in the end, in this case will prevent a new line

