class Employee:
    def read_emp_value(self):
        self.eno = int(input("Enter Employee Number: "))
        self.name = input("Enter Employee Name:")
        
class Student:
     def read_stud_value(self):
        self.eno = int(input("Enter Student Number: "))
        self.name = input("Enter Employee Name:")
    

        
        


class PrintData:
    #@staticmethod
    #@classmethod
    def display_object_data(self, obj):
        for k,v in obj.__dict__.items():
            print(f"{k}===>{v}")

p =PrintData()
Emp1 = Employee()
Emp1.read_emp_value()
print(id(Emp1))

print(id(p.display_object_data(Emp1)))
Stud1=Student()
Stud1.read_stud_value()
print(id(p.display_object_data(Stud1)))
