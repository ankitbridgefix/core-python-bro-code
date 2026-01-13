class Student:
    @classmethod
    def course(cls):
        cls.crs = "Python"
        
    def get_value(self):
        self.stno =int(input("Enter Student Number:"))
        self.name =input("Enter Student Name:")
    
    def disp(self):
        Student.course()
        print("Student Number :{}".format(self.stno))
        print("Student Name :{}".format(self.name))
        print("Student Course :{}".format(self.crs))
    

s1 = Student()
s1.get_value()
s1.disp()

        