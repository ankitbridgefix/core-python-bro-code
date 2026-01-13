from menu import Menu
def add():
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    c = a+b
    print("Sum of {}+{}={}".format(a,b,c))

def sub():
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    c = a-b
    print("Sub of {}-{}={}".format(a,b,c))

def mul():
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    c = a*b
    print("Mul of {}*{}={}".format(a,b,c))

def div():
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    c = a/b
    print("Div of {}/{}={}".format(a,b,c))