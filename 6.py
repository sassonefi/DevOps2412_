# loops

for i in range(5):
    print("hello " + str(i))
else:
    print("finished")
    
class_mates = ["maksim", "yoni", "gilad", "oren"]
for name in class_mates:   # for each loop
    if name == "yoni":
        name = "amir"
    print(name)

for i in range(len(class_mates)): # loop by index. use if you need to use it later on
    print(class_mates[i])

your_name = input("enter your name: ")
while your_name != "aviel":  #while loop
    print("you are not aviel")
    if your_name == "haim":
        print("omg")
        break # loop finished
    if your_name == "david":
        print("wow")
        #continue # continue will create endless loop in this case
    your_name = input("enter you name: ")