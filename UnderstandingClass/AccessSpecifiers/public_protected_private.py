# If a member(data or method) is public it can be accessed within and from outside of a class. Every member of a python class is by default public
# In python public private and protected are not implemeneted but using some convention we can use it as public private and protected
#Public
class AccessModifier:
    def __init__(self,instance_var):
        #instance var is public as its access outside of var
        self.instance_var = instance_var
    #Method is public as its accessed from outside   
    def m1(self):
        print("value of instance var {}".format(self.instance_var))
        
obj = AccessModifier(5)
# m1 Method is public as its accessed from outside  
obj.m1()
print(obj.instance_var)
obj.instance_var =10
print(obj.instance_var)

#Private
#If a memeber is accessed only within the class then its called as private
#private member are declared by prefixing __membername 
class PrivateModifier:
    __var = 30
    def __init__(self,instance_var):
        #instance var is public as its access outside of var
        self.instance_var = instance_var
    #Method is public as its accessed from outside   
        
    def __privatemethod(self): 
        print("value of instance var from private method {}".format(self.__var))
    def m1(self):
        self.__privatemethod()
        print("value of instance var",self.instance_var)
        
obj = PrivateModifier(5)
#print(obj.__var) -> ERROR since it cant call private member from outside class
obj.m1()


# NAME MANGLING; Every private member get an alias name of objectreference._CLASSNAME__membername. Through this way once can access private member outside of a class
print(obj._PrivateModifier__var)


#PROTECTED 
#Members can be accessed within the class and only from child class
#HOw to declare a protcted member. Use one undersore in suffix e.g. _membername
#Note protected is also just a naming convention, however we can access the single underscore membername from outside class
class protected:
    _varname = 8
    def m1(self):
        print(self._varname)
        
obj_protected = protected()
print(obj_protected._varname)