
class ConcreteWheel:
    def turn(self):
        print("Using Wheel")
        return "Using Wheel"
## Car ---DEPENDS---> ConcreteWheel 
class Car:
    def __init__(self, ObjectThisDependsOn):
        self.Wheel = ObjectThisDependsOn
        self.turning = True

    def getState(self):
        if self.turning == True:
            self.Wheel.turn()
        return 0
    
testCar = Car(ConcreteWheel())
testCar.getState()

#The problem with tight coupling is new objects with different specifications
# "newturn" instead of "turn"
class NewConcreteWheel:
    def newturn(self):
        print("Using new Wheel")
        return "Using new Wheel"

try:
    testCar = Car(NewConcreteWheel()) #breaks
    testCar.getState()
except Exception:
    print("Failed due to new object having different specification 'newturn'")




#REFACTOR
from abc import ABC, abstractmethod

class AbstractWheel(ABC): #ABC as argument tells us this is an abstract class
    #also make an abstract method
    @abstractmethod
    def turn(self):
        pass

#refactor the class to implement the abstract class/Interface
#python passes the abstract class for implementation
class ConcreteWheel(AbstractWheel): #ConcreteWheel ---Implements---> AbstractWheel
    def turn(self):
        print("Using Wheel")
        return "Using Wheel"

#Car ---DEPENDS---> AbstractWheel   , The Abstraction weakens the tight coupling
class Car:
    def __init__(self, WheelInterfaceImplementation):
        self.Wheel = WheelInterfaceImplementation
        self.turning = True

    def getState(self):
        if self.turning == True:
            self.Wheel.turn()
        return 0

testCar = Car(ConcreteWheel())
testCar.getState()
#What dependency inversion does, is force the new class to implement "turn"
class NewConcreteWheel(AbstractWheel): #NewConcreteWheel ---Implements---> AbstractWheel
    def newturn(self):
        print("Using new Wheel")
        return "Using new Wheel"
    def turn(self): #FORCES "turn" implementation
        print("Using new Wheel")
        return "Using new Wheel"
testCar = Car(NewConcreteWheel())
testCar.getState()
