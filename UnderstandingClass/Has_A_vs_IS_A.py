#Employee is-A relationship with person class
#Employee has a relationship with car

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def eatdrink(self):
        print("person can eat and drink")

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
        
    def getCarInfo(self):
        print("Car info: \n\tname:{} \n\tmodel:{}, \n\tcolor:{}".format(self.name,self.model,self.color))
                
class Employee(Person):
    def __init__(self,name,age,emp_no,emp_sal,car_obj):
        super().__init__(name,age)
        self.emp_no = emp_no
        self.emp_sal = emp_sal
        self.car_obj = car_obj
        
    def canWork(self):
        print("Employee can work")
        
    def getEmpInfo(self):
        print("Employee name ",self.name)
        print("Emp Age ",self.age)
        print("Emp no", self.emp_no)
        print("Emp sal ",self.emp_sal)
        self.car_obj.getCarInfo()
      

        
car_obj = Car("Hyundai", "i10 Nios", "Red")
emp_obj = Employee("abhi", 38, 21, 2000, car_obj)
emp_obj.getEmpInfo()
emp_obj.canWork()
emp_obj.eatdrink()
         