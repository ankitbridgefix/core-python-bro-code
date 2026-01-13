class Student:
    def __init__(self,n,r):
        self.name =n
        self.roll = r
        
    def disp(self):
        print("Name:{} And Roll:{}".format(self.name,self.roll))
        
class User:
    @staticmethod
    def show(s):
        print("Show Name:{} And Show Roll:{}".format(s.name,s.roll))


stu = Student("Ravi",16153278)        
#stu.disp()
User.show(stu)
