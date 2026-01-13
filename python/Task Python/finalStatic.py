from datetime import date
class Person:
    company = "GOOGLE"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #print(f"NAME:{self.name} and AGE:{self.age} and COMPANY NAME:{self.company}")
        self.email = name+"@gmail.com"
    @property
    def email(self):
        return f"{self.name}@gmail.com"
    @email.setter
    def email(self,newEmail):
        self.name = newEmail.split("@")[0]
    
    def get_details(self):
        print("*"*60)
        print(f"NAME:{self.name} and AGE:{self.age} and COMPANY NAME:{self.company} Email:{self.email}")
        print("*"*60)
    
    @classmethod   
    def fromDoByear(cls,name,year):
        return cls(name,date.today().year-year)
    @classmethod
    def Change_Company_Name(cls,NewName):
        cls.company = NewName
    @staticmethod   
    def isAdult(age):
        return age>=18
    
Person.Change_Company_Name("APPLE")
# print(p1.age)
p1 =Person("Ravi",251)
p2 =Person.fromDoByear('Ram',2020)
print(p2.email)
print(Person.company)
p2.Change_Company_Name("infosys")
print(p2.company)
print(Person.company)
p2.email="Rahul@gmail.com"
p2.get_details()
print(p2.email)
print(Person.isAdult(p2.age))
print(p2.name)


# from menu import Menu_fun
# import sys

# while True:
#     Menu_fun()
#     ch = int(input("Enter You Want Operation:"))
#     p2 =Person.fromDoByear('Ram',2020)
#     if ch==1:
#         p2.get_details()
#     elif ch==2:
#         newCompanyName = input("Enter New Company Name:")
#         Person.Change_Company_Name(newCompanyName)
#     elif ch==3:
#         newEmail = input("Enter New Email:")
#         p2.email = newEmail
#         p2.get_details()
#     elif ch==4:
#         print("*"*50)
#         print("Adult Status:",Person.isAdult(p2.age))
#         print("*"*50)

#     elif ch==5:
#         print("***** THANKYOU ****")
#         sys.exit()
#     else:
#         print("Wrong Choice")
        
        
import pdb; pdb.set_trace()