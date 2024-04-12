class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
        
    def getCarInfo(self):
        print("Car info: \n\tname:{} \n\tmodel:{}, \n\tcolor:{}".format(self.name,self.model,self.color))
        
class Employee:
    def __init__(self,emp_name,emp_no,car_obj):
        self.emp_name = emp_name
        self.emp_no = emp_no
        self.car_obj = car_obj
        
    def getEmpInfo(self):
        print("Employee name {} \nEmp no {} ".format(self.emp_name,self.emp_no))
        self.car_obj.getCarInfo()
        #print("Employee name {} \nEmp no {} \nCar info: {} ".format(self.emp_name,self.emp_no,self.car_obj.getCarInfo()))
        #It prints None for self.car_obj.getCarInfo()
        #Reason: In Python, when a function or method does not explicitly return a value, it implicitly returns None.
car_obj = Car("Hyundai", "I10 Nio", "Blue")
emp_obj = Employee("Abhi", 123 , car_obj)
emp_obj.getEmpInfo()
        
#In Python, when a function or method does not explicitly return a value, it implicitly returns None.


def Test():
    print("I am in test")
    
print("Lets Test return value of Test function {}".format(Test()))