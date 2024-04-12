#!/usr/bin/python
import time
def decorator_fun(original_fun):
    def wrapper_fun(*args):
        start_time=time.time()
        print("Before original function is called {}".format(original_fun.__name__))
        print("After original funcation is called {}".format(original_fun(*args)))
        print("time difference {}".format(time.time()-start_time))
    return wrapper_fun
    
@decorator_fun    
def add(x,y):
    return x+y
    
add(2,3)