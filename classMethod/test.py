class MyClass():

    TOTAL_OBJECTS=0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS+1

    @classmethod
    def total_objects(cls):
        print("Total objects: ",cls.TOTAL_OBJECTS)

# Creating objects of parent class
my_obj1 = MyClass()
my_obj2 = MyClass()


# Creating a child class
class ChildClass(MyClass):
    TOTAL_OBJECTS=0
    def __init__(self):
        ChildClass.TOTAL_OBJECTS = ChildClass.TOTAL_OBJECTS+1

    #pass
my_obj3 =ChildClass()

MyClass.total_objects()
ChildClass.total_objects()

