class Book:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        total_pages = self.pages + other.pages
        return Book(total_pages)
    
    def __str__(self):
        #return "Total no of pages {}".format(self.pages)
        return str(self.pages)
        #The reason why __str__ should return only a string value is because it is intended to provide a textual representation of an object.
    
    def __gt__(self,other):
        return self.pages > other.pages
    
    def __ge__(self,other):
        return self.pages >= other.pages
#Add pages of books
b1 = Book(100)
b2 = Book(200)
print(b1+b2) 
# + is overloaded to add two objects and its possible using a special magic method __add__() which accepts two argunment
#self pointing to first obejct and other poiting to second object
b3 = Book(400)
print(b1+b2+b3) # It will fail as first b1 and b2 is passed which returns an int value and then int and b3 obect is passed and int and 
#pbject is a mismatch and cannot be added. To avoid this issue we need to return an object insted of int. Now print will give some meaningless return
#<__main__.Book object at 0x0000019E5836BD00>. To make it meaningful again we have to use one more magic function __str__ which gives meaningful output

#operator overloading for > using __gt__() magic method.
#Note: if we are using __gt__() then __lt__() is not required
print(b1>b2)

#operator overloading for >= using __gt__() magic method.
print(b1>=b2)