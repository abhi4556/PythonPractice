#/usr/bin/python
class Employee:
    raise_pay = 1.05
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        name = self.first + " " +  self.last
        return name

class Developer(Employee):
    def __init__(self,first,last,pay,lang = None):
        super().__init__(first,last,pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def list_of_emp(self):
        for emp in self.employees:
            print("Employee full name {}".format(emp.full_name()))
            print("Employee pay {}".format(emp.pay))


dev1 = Developer("Abhi","Mukherjee",5000)
dev2 = Developer("Pari","mukherjee",10000,"Python")
mgr1 = Manager("Luci","troy",20000,[dev1,dev2])
#mgr1.add_employee(dev1)
#mgr1.add_employee(dev2)
print(mgr1.full_name())
mgr1.list_of_emp()
#print(dev1.full_name())
#print(dev2.lang)
print(isinstance(mgr1,Manager))
print(issubclass(Manager, Employee))