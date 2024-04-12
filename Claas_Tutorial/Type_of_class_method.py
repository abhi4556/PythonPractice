#/usr/bin/python
'''
Method: Method consisting of instance/object/self as default argument is called normal method

Class Method: Methid which except class as default argument

Static Methid: Method which neither have instance nor object as argument is called as Static Method

Question: In which scenarion we define method as static
Answer: When we neither using instance variable nor class variable so such method we can decalare as static method

Question: Any example where we can use class method?
Answer: If user input parameter is not allign with the constructor then we can define a class method which modifies the input to align with the conestructor
'''


class Employee:
    def __init__(self,first,last,email):
        self.first = first
        self.last = last
        self.email = email

    
    def display(self):
        print("First: {} \nlast: {} \nemail {}".format(self.first,self.last,self.email))

    @classmethod
    def format_input( cls, data_str):
        first,last,email = data_str.split('-')
        return cls(first,last,email)
        #return Employee(first,last,email)

    #@staticmethod
    def which_day(day):
        if day == "Saturday" or day == "Sunday":
            return "Weekend"
        return "Weekday"


emp1 = Employee("Abhi","Mukherjee","abhijit.myworld@gmail.com")
emp1.display()
emp_str = "Abhi-Mukherjee-abhijit.myworld@gmail.com"
new_emp1 = Employee.format_input(emp_str) #calling class method to alling user input to constructor
print("Email {}".format(new_emp1.email))
day = "Saturday"
print(Employee.which_day(day))

