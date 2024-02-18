a = 50
b = 10
my_name = "aviel"
if b >= 10 or a < 10: # can do if not for negative
    print("you are avielb")
    print("hello")
elif my_name == "aviel":
    print("b is good")
elif b > 5:
    print("found your name")
else:
    print("blabla")

print(a == 50) #will print True
should_i_work_today = a == 50 and b < 100 #should_i_work is a boolean
if should_i_work_today:
    print("go to work")
else:
    print ("stay at home")


my_list = [] # since list is empty the boolean is set to false
if len(my_list): # check the length, return integer
    print("you have items")
else:
    print("no item in the list")


my_other_list = ["or" , " tohar" , "adam"]
my_other_name = "moshe"

if my_other_name in my_other_list: # check if moshe is inthe list
    print("i found it")

tt = 50
rr = 50
print(tt is rr)

tt = [1, 2, 3]
rr = [1, 2, 3]
print(type(tt) is list) #check the type of tt and check if this is a list


