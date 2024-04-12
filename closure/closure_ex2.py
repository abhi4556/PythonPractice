#!/usr/bin/python
import logging
logging.basicConfig(filename="example.log", level=logging.INFO)

def logger(fun):   #remeber the add function and stores it reference in fun variable
    def inner_fun(*args):  # when inner fun is called it knows the fun variable is pointing to add function,
        print(fun.__name__)  
        logging.info("Running {} with arguments {}".format(fun.__name__,args))
        print(fun(*args))  #its same as print(add(x,y))
    return inner_fun

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

call_inner = logger(add)  #logger function return the reference of inner_fun, so call_inner is pointing to inner_fun
call_inner(5,6)  #here we are calling inner_fun with two parameter, so inner_fun must except these parameter hence *args is present inner_fun(*args)
'''
#step by step explanation
1> call_inner = logger(add)  -> logger(add) it calls a function logger with argunment as function add,  in logger function , fun is a reference which is pointng to function add
                                and logger then return an inner_fun.
                                During this process closure inner_fun create a reference fun which is pointing to function add.
2> call_inner(5,6) -> call_inner is now pointing to inner_fun so we are calling inner_fun with argunment as 5,6 which is tored in args

'''