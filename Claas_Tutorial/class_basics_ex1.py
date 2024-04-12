#/usr/bin/python
class Vehicle:
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price
    def display(self):
        print(" Name: {} \n model: {} \n price: {}".format('name','model','price'))


obj_vehicle1 = Vehicle("Maruti", "2012", "100000")

'''
Both the call are correct. One has the default call to claas init methid with passing objec to self
Here we are calling the display fyunction of class explicitly passing the obj to self
'''
#obj_vehicle1.display()
Vehicle.display(obj_vehicle1)
