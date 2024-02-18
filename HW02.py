#HW for L#02 31.12.23
#A

x = 2
y = 0
if x > y:
    print("Big")
elif x < y:
    print("small")
else:
    print("equal")

#B
for i in range(5):
    print(i)

#C
for i in [1, 2, 3, 4]:
    if i == 1:
        print(str(i) + " = summer")
    elif i == 2:
        print(str(i) + " = winter")
    elif i == 3:
        print(str(i) + " = fall")
    elif i == 4:
        print(str(i) + " = sprint")

#D
#1. 10 time
#2. 10 will be printed last
count = 1
while count < 11:
    print(count)
    count = count + 1

#E
details = [45, "s", 3.64, True, 19]
print(details)
result = details[0] + details[2]
print(result)

#F
phone_number = input("what's you phone number? ")
print("phone number: " + str(phone_number))

#G
def printHello():
    print("Hello")
def calculate():
    result = 5 + 3.2
    print(result)

printHello()
calculate()

#H
def myName():
    name = input("what's you name? ")
    print(name)

myName()

def divBy2():
    num = int(input("write a number: "))
    print(int(num/2))

divBy2()

#I
def numSum(num1, num2):
    result = num1 + num2
    print(result)

numSum(3, 5)

def spaceStrings(str1, str2):
    print(str1+" "+str2)

spaceStrings("what's", "up")

#K
for i in [1, 2, 3, 4, 5]:
    print("*" * i)

#L
# for i in [1, 2, 3, 4, 5, 6, 7]:
#     print("*" * i)
