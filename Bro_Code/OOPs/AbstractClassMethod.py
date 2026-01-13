from abc import ABC,abstractmethod

class Vehical(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehical):
    def go(self):
        print("Car Is go")

class Motorcylcle(Vehical):
    def go(self):
        print("motor Cycle is go")
   # pass
        
    
#velical = Vehical()
car = Car()
car.go()

mo = Motorcylcle()
#mo.go()