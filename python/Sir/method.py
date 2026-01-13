from datetime import date as dt
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    @staticmethod
    def isAdult(age):
        if age >18:
            return True
        else:
            return False
    @classmethod
    def emp_from_year(cls, name, year):
      return cls(name, dt.today().year - year)
    
    def __str__(self):
      return 'Employee Name: {} and Age: {}'.format(self.name, self.age)
        
    
d =Employee.emp_from_year("Rahul",2020)
print(d)