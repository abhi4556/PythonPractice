#!/usr/bin/python

import time

def timer_decorator(fun):
    def wrapper(*args):
        start_time = time.time()
        print("Time before calling add fun {}".format(start_time))
        print("Add function is called {}".format(fun(*args)))
        print("Time after add function is called {}".format(time.time()-start_time))
    return wrapper

@timer_decorator
def add(x,y):
    return x + y

add(4,5)