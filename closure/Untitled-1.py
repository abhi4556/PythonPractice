#!/usr/bin/python

import time


def timer_decorator(fun):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print("Time before calling add fun {}".format(start_time))
        print("Add function is called {}".format(fun(*args)))
        end_time=time.time()
        print("End time: {}".format(end_time))
        print("Difference in time between before and after add function is called {}".format(end_time-start_time))
    return wrapper

@timer_decorator
def add(x,y):
    return x + y

add(4,5)