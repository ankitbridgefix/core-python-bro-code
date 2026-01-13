class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# my = MyClass()
# print(my.method())
# print(my.classmethod())
# print(MyClass.staticmethod())

class Employee:
    no_of_emp = 0
    raise_amt = 1.04
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname =lname
        self.pay = pay
        Employee.no_of_emp +=1
    def full_name(self):
        print("{} {}".format(self.fname,self.lname))
        
    def apply_raise(self):
        return self.pay * self.raise_amt
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    @classmethod    
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split("-")
        return cls(first,last,pay)

emp1 = Employee("Ankit","patidar",5000)
emp2 = Employee("Ram","Raghukul",6000)
emp2.set_raise_amt(1.08)
print(emp1.apply_raise(),"==",emp1.raise_amt)
print(emp2.apply_raise(),"==",emp2.raise_amt)
print(Employee.raise_amt)

emp_str1 = "John-doe-2000"
emp_str2 = "Steve-smith-4000"
f=Employee.from_string(emp_str1)
f.full_name()



# print(emp1)
# emp1.full_name()
# print(Employee.full_name(emp1))
