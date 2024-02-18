# import requests
# try:
#     requests.get("adsdsd.?:ssddsdsds")
# except BaseException as e: #will continue with the code if the code in the try doesn't work
#     print("something went wrong")
#     print(e.args)
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# result = a / b
# print(result)

#2nd example
while True:
    try:
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        result = a / b
        print(result)
        break
    except ValueError:
        print("enter a correct number")
    except ZeroDivisionError:
        print("could not divide by zero")
    except BaseException as e:
        print(e.args)