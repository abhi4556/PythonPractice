#!/usr/bin/python

import logging
import time
logging.basicConfig(filename='Ex3.log', level = logging.INFO)
from functools import wraps
#logging.info("Testing")

def logger(original_func):
    @wraps(original_func)
    def wrapper_fun(*args,**kwargs):
        logging.info("{} and args are {}".format(original_func.__name__,args))
        return original_func(*args,**kwargs)
    return wrapper_fun

def timer(original_func):
    @wraps(original_func)
    def wrapper_func(*args,**kwargs):
        #import time
        t1 = time.time()
        original_func(*args,**kwargs)
        t2 = time.time() - t1
        print("total time taken to execute {} is {}".format(original_func.__name__,t2))
    return wrapper_func
""" @logger
def display(name,age):
    print ("name is {} and age is {}".format(name,age)) """
@timer
@logger
def display(name,age):
    time.sleep(3)
    print ("name is {} and age is {}".format(name,age))


display("Abhi",35)
