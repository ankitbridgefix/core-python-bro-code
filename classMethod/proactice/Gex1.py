from datetime import date

class Person:
    company = "Apple"
    def __init__(self,name,age):
        self.name =name
        self.age =age
    @property   # no need to () in call
    def get_details(self):
        print(f"Emplyee Name:{self.name} and Age:{self.age} and Company Name:{self.company}")
    @classmethod
    def Person_birth_year(cls,name,year):
        return cls(name,date.today().year-year)
    
    @classmethod
    def Change_Company_Name(cls,newName):
        cls.company = newName
        
    @staticmethod
    def isAdult(age):       
        return age>18

a=Person("Ankit",24)
a.get_details
#####
person2=Person.Person_birth_year("Rahul",2020)
print(a.age)
print(person2.age)
print(Person.isAdult(person2.age))
a.Change_Company_Name("Google")
print(a.company)
print(Person.company)
a.get_details


