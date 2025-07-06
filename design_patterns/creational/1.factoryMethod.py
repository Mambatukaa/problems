"""
There’s an interface or an abstract class with multiple concrete implementations. It represents an object that needs to be created (let’s call it a Target Object).
There’s a concrete implementation of Factory per each concrete implementation of the Target Object.
When we need to return a specific implementation of the Target Object, we initialize a specific implementation of Factory and call the creation method on it.


An abstract product (Vehicle)

Multiple concrete products (Car, Bike)

An abstract factory (VehicleFactory)

Concrete factories (CarFactory) that produce specific products

Your client only needs to use the factory, not care about which Vehicle is being created behind the scenes.

"""
from abc import ABC, abstractmethod


# abstract product
class Vehicle(ABC):
    @abstractmethod
    def getType(self):
        pass

# concrete product
class Car(Vehicle):
    def getType(self):
        return "car"
    

class Bike(Vehicle):
    def getType(self):
        return "bike"



# abstract factory
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle: 
        pass


# concrete factory
class CarFactory(VehicleFactory):
    """ Overrides createVehicle to return car"""
    def createVehicle(self):
        return Car()


carFactory = CarFactory()

print(carFactory.createVehicle().getType())
