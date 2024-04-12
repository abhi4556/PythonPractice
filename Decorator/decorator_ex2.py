#why we need a decorator
#So whenver we need some functionality to be executed before our original function is called we can use of a decorator

""" def decorated_dispaly(original_fun):
    def wrapper_fun():
        print("wrapper executed this before {} is called ".format(original_fun.__name__))
        return original_fun()
    return wrapper_fun

def display():
    print("Display is called")

decorated_fun = decorated_dispaly(display)
decorated_fun() """

#writing above code in simpilar way

def decorated_dispaly(original_fun):
    def wrapper_fun(*args,**kwargs):
        print("wrapper executed this before {} is called ".format(original_fun.__name__))
        return original_fun(*args, **kwargs)
    return wrapper_fun

@decorated_dispaly #its same as decorated_fun = decorated_dispaly(display)
def display():
    print("Display is called")

#display()

@decorated_dispaly
def display_info(name,age):
    print("Name is {} and age is {}".format(name,age))

display_info('Abhi', 35)