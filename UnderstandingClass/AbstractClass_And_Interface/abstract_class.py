#Abstract class: Which never talks complete information

#Abstract class is partially implemenetd class
#Note: Its mandatory for child class to give defination to the abstract method
# ABC : Abstract base class
# ABC class present inside abc module

#ABSTRACT METHOD
#Method which only have declaration and not implemenetation
#Abstract method syntax is to have @abstractmethod decorator

#ABSTRACT CLASS
#Abstract class must be a child class of ABC

#By having an abstaract class we provide gudeleines to child class to provide implemenetation to abstarct method

from abc import abstractmethod,ABC
#abstract method is implemented in abc module
class Vehicle(ABC):
    #Vehicle is an abstarct class here as its inheretied from ABC class
    # Since I dont know the type of vehicle so i dont know the no of wheels
    @abstractmethod
    def getNoOfwheels(self):
            pass
    
    def getNoOfStering(self):
        return 1
  
class Bus(Vehicle): 
    def getNoOfwheels(self):
        return 6

class Auto(Vehicle):
    def getNoOfwheels(self):
         return 3
    
#you cant create an object of an abstract class         
#vehicle_obj = Vehicle()
bus_obj =Bus()
auto_obj = Auto()
print(bus_obj.getNoOfwheels())
print(auto_obj.getNoOfwheels())


    