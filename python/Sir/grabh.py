class A:
    def __init__(self,name):
        self.name= name
        print(self.name)
    
        
    
    # def disp(self):
    #     print("THis is Simple METHOD Method")
    #     b=20
    #     print(b)
    # @staticmethod
    # def disp1():
    #     print("This is Static method")
    
    @classmethod
    def disp2(self,name):
        print("THis is class method",name)
        return name
    
    def __str__(self):
        return 'Employee Name: {} '.format(self.name)
            
#NORMAL 
print("============Print Simple Method ===============")
# d = A() # WORKING
# d.disp() #wORKING
# c =d.disp()
#A.disp() # NOT WORKING
print("============Print Static===============")
#A.disp1()
print("============Print Class Method==========")
#A.disp2("Ankit")
d =A("ddd")
print(d.disp2("cd"))
