
import sys
from operration import add,sub,mul,div,Menu

while True:
    Menu()
    try:
        ch = int(input("Enter Your Choice:"))
    except ValueError:
        print("Please Enter Number")
    else:
        if ch==1:
            add()
        elif ch==2:
            sub()
        elif ch==3:
            mul()
        elif ch==4:
            div()
        elif ch==5:
            print("Thanks For Using Calculator:")
            sys.exit()
        else:
            print("Please choose correct Input:")

