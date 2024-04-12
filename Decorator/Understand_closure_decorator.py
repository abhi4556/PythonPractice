#/usr/bin/python
'''
Example of a closure. It shows whatever argunment we have passed to decorator_fun it memorizes the variable and when we call th einner function
it uses the memorized variable in inner funaction/wrapper_fun
'''
def decorator_fun(msg):  #Hi passed is memorized
    def wrapper_fun():
        print("Message {}".format(msg))
    return wrapper_fun

call_wrapper = decorator_fun("Hi")  #gets the wrapper_fun as return 
call_wrapper()  # Calling the wrapper_fun

call_wrapper_again = decorator_fun("Bye")
call_wrapper_again()

'''
Closure conecpt is implemented in decorator
Instead of passing an value as an argunment. Now a method name is passed as an argunment
'''
def decorator_function(original_func):
    def wrapper_function():
        return original_func()
    return wrapper_function

def display():
    print("Display is called")

decorated_dispaly = decorator_function(display) # Its calling a decorator_fun and return a wrapper_fun
decorated_dispaly()  # Its basically calls a wrapper_fun
'''

'''
def decorator_function(original_func):
    def wrapper_function():
        return original_func()
    return wrapper_function

@decorator_function  #@decorator_function <=> display = decorator_function(display)
def display():
    print("Display is called")
# Line 29 and 30 is also written as line 42 and 43

display()