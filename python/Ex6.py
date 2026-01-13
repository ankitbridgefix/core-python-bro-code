"""n=int(input())
x=int(input())
y=int(input())
z=int(input())"""

"""newlist = [[i,j,k] if i+j+k!=5 else "no"  for i in range(1,4) for j in range(1,4) for k in range(1,4)  ]
print(newlist)"""

"""def First(text):
    print(text.title())

a=First
print(type(a))
a("ankit")"""

"""def Upper(text):
    return text.upper()
def Lower(text):
    return text.lower()
def Call_f(func):
    greeting = func("Hello Ankit hwu where are you")
    print(greeting)
    
Call_f(Upper)
Call_f(Lower)"""


"""def Outer_func(x):
    print("Run Outer Function")
    def Inner_func(y):
        print("RUN INNER FUNCTION")
        return x*y
    return Inner_func

in1 = Outer_func(9)

j =in1(10)
print(j)
"""
# importing "math" for precision function
import math

# initializing value
a = 3.52

# using trunc() to print integer after truncating
print("The integral value of number is : ", end="")
print(math.trunc(a))

# using ceil() to print number after ceiling
print("The smallest integer greater than number is : ", end="")
print(math.ceil(a))

# using floor() to print number after flooring
print("The greatest integer smaller than number is : ", end="")
print(math.floor(a))
"""import math
print(math.floor(200.25))
print(math.ceil(20.00000))
"""



    
    