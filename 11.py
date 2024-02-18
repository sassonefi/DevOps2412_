#functions

for i in range(5):
    print("hello " + str(i))

for i in range(10):
    print("you are number " + str(i))

def my_printer(prefix, amount_of_times):   # define function
    for i in range(amount_of_times):
        print((prefix + str(i)))

def mul_five(my_number):
    result = my_number * 5
    return result

if mul_five(10) > 1:
    my_printer("more then ", 10)

the_result = mul_five(10)
print(the_result)

# my_printer("hello ", 5)
# my_printer("you are number ", 10)