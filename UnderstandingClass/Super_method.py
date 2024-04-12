class Parent:
    a = 10
    def __init__(self):
        print("In parent constructor")
    def m1(self):
        print("In Parent instance method")
        
    @classmethod
    def m2(cls):
        print("In parent class method")
        
    @staticmethod
    def m3():
        print("Parent static method")
        
class child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")
        
    def method(self):
        print(self.a)
        self.m1()
        self.m2()
        self.m3()
        
child_obj = child()
child_obj.method()