class Car:
    color = None

def change_color(car,color):
    car.color = color

class MotorCycle():
    color = None

car1 = Car()
car2 = Car()
print(car1.color)
change_color(car1,"red")
print(car1.color)
print(car2.color)

bike1 = MotorCycle()

change_color(bike1,"blue")
print(bike1.color)
print(MotorCycle.color)


