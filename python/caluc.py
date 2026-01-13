import sys
class Calculator:
    def __init__(self,a,b):
        self.a =a
        self.b =b
        
    def Add(self):
        self.res =self.a+self.b
        return self.res
    
    def Sub(self):
        self.res =self.a-self.b
        return self.res
    
    def Mul(self):
        self.res =self.a*self.b
        return self.res
    def div(self):
        self.res = self.a/self.b
        return self.res
while(True):    
    a = input("Enter Fist Number:")
    b= input("Enter Second Number:")
    if(a.isalpha() or b.isalpha()):
        print("Please Enter Number Value:")
    
    elif(a.isdigit() and b.isdigit()):
        a =float(a)
        b=float(b)
        if(a>=0 and b>=0):
            obj = Calculator(a,b)
            op =input("Please Enter CHoose + OR - OR * OR /: \n")
            if(op=="+"):
                print("Result: ",obj.Add())
                print("Thanks for using this calculator:")
                a =input("You Want Exit Plese Enter YES:")
                if(a=="YES"):
                    sys.exit()
            elif(op=="-"):
                print("Result: ",obj.Sub())
                a =input("You Want Exit Plese Enter Y:")
                if(a=="Y"):
                    sys.exit()
            elif(op=="*"):
                print("Result: ",obj.Mul())
                a =input("You Want Exit Please Enter YES:")
                if(a=="YES"):
                    sys.exit()
            elif(op=="/"):
                print("Result: ",obj.div())
            else:
                print("you are enter Wrong Operator")
        else:
            print("Please Enter Positive Number:")
    else:
        print("*"*30)    
        print("Please Enter Valid Input") 
        print("*"*30)   
                