import sys
class Calculator:
    def Exit(self):
       print("*"*50)
       self.e = input("You Want TO Exit Press Y:\nYou Want TO Continue Press Any Key:\n")
       if(self.e=="Y" or self.e=="y"):
            print("Thankyou Visit Again")
            sys.exit()  

    def get_val(self):
        try:
            self.num1 =float(input("Enter First Value:"))
            self.num2 =float(input("Enter Second Number:"))
            return True

        except ValueError:
           print("please enter a valid values")
           return False

    def Add(self):
        print("Result: ",self.num1+self.num2)
       
    
    def Sub(self):
            print("Result: ",self.num1-self.num2)
        
            
    def mul(self):
        try:
            #self.get_val()
            print("Result: ",self.num1*self.num2)
        except AttributeError:
            print("Please Enter Number Values")
            print("*"*50)
        
    def Div(self):
        try:
            #self.get_val()
            print("Result: ",self.num1/self.num2)
        except AttributeError:
            print("Please Enter Number Values")
            print("*"*50)
        
        except ZeroDivisionError:
            print("Do not Enter Zero")
            print("*"*50)
            
                
c =Calculator()

get_num = c.get_val()

v_o =['+','-','*','/']
while True:
    if get_num:
        while True:
            ch =input("Please Enter + OR - OR * OR /: \n")
            if ch in v_o:
                if ch=="+":
                    c.Add()
                    c.Exit()

                    break
                elif(ch=="-"):
                    c.Sub()
                    c.Exit
                    break
                
                elif(ch=="*"):
                    c.mul()
                    c.Exit()
                    break
                elif(ch=="/"):
                    c.Div()
                    c.Exit()
                    break

                
        