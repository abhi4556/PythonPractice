class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name = name
        self.dob= DOB(dd,mm,yyyy)
        
    def info(self):
        self.dob.display()
    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy
            
        def display(self):
            print("Dob {}/{}/{}".format(self.dd,self.mm,self.yyyy))
            
p = Person('Abhi',17,8,1986)
p.info()