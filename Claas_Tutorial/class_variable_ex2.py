#/usr/bin/python
class Vehicle:
    inc_in_price = 2
    no_of_vehicle = 0
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price
        Vehicle.no_of_vehicle += 1
        print("I am in init")
    def display(self):
        print(" Name: {} \n model: {} \n price: {}".format('name','model','price'))
    def inrease_price(self):
        print("old price {} ".format(self.price))
        print("New price {}".format(int(self.inc_in_price)*int(self.price)))



obj_vehicle1 = Vehicle("Maruti", "2012", "100000")
obj_vehicle2 = Vehicle("Maruti", "2012", "400000")
print("No of vehicle{}".format(Vehicle.no_of_vehicle))
print(obj_vehicle1.inc_in_price)
print(Vehicle.inc_in_price)
'''
Since inc_in_price is a class variable then why we also access it using object/self (self.inc_in_price)
 Note: When we try to access an attribute from an instance first it checks if the instance contains the atrribute if not then it checks if the class contains that attributre
'''
obj_vehicle1.inc_in_price = 4
'''
When we change the class variable using an instance it means it only changes the claas variable in its own scope. It doesnt change the class variable for other instance
'''
print(obj_vehicle1.__dict__)
#{'name': 'Maruti', 'model': '2012', 'price': '100000', 'inc_in_price': 4}
print(obj_vehicle2.__dict__)
#{'name': 'Maruti', 'model': '2012', 'price': '400000'}
