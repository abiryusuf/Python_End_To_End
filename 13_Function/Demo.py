
"""
Function is a block of codes that will run when we call it
we can pass the data in the parameters into a function
"""
# def fac(n):
#     s = 1
#     for i in range(1, n):
#         s += i * 2
#     print(s)
#
# fac(5)

def myFunction(x, y):
    return "First Name " + x + " Last Name " + y

print(myFunction("Abir", "Yusuf"))

def my_function(**name):
    print("First Name " + name["lname"])

my_function(fname="Mim",  lname="Jim")

def function_3(country="Bangladesh"):
    print("I am from " + country)
function_3("USA")

name = ["Mim", "Jim", "Kim"]
def function_4(str):
    for i in str:
        print(i)
function_4(name)
