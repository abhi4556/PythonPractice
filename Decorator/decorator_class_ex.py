class decorator_class(object):
    def __init__(self,original_fun):
        self.original_fun = original_fun
    
    def __call__(self,*args,**kwargs):
        print("Call method called {}".format(self.original_fun.__name__))
        return self.original_fun(*args,**kwargs)
  
 # Functionalty is same only think outer funaction changed to class and inner function changed to __Call__   
@decorator_class
def display():
    print("Display method executed")
    
@decorator_class
def display_info(name,age):
    print("Dispaly with argunment {} {}".format(name,age))
    
display()
display_info('abhi', '37')