
def addNames (name1, name2, name3):
    #my_names = open("names.txt", 'a+')
    with open('example.txt', 'a+') as file:
        # Write text to the file
        file.write("name1", "name2", "name3")

def printName():
    my_file = open("names.txt")
    for name in my_file.readlines():
        print(f"hello {name}", end='')

addNames("a", "b", "c")
printName()