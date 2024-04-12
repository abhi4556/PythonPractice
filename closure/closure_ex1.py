#/usr/bin/python
# what is a closure
# A closure is an inner function which remeber the free variable or variable defined in outer function even after the outer function has finsished executing
# the closure in a decorator remembers variables defined in the outer function by maintaining references to those variables, 
# allowing them to be accessed and used even after the outer function has completed its execution.

#Here inner_func implementation is a closure
#EX1
def outer_func():
    message = "Hi"
    def inner_func():
        print (message)
    return inner_func

msg = outer_func()  # Here outer function exists but still remember the free variable value
msg()  #calling the alias of inner function and it still remeber the free variable value


#EX2
#closure with an argument

def greeting(msg):
    def helper_func():
        print("Message is {}".format(msg))
    return helper_func

call_helper = greeting("Hi")
call_helper()
call_new_helper = greeting("Hello")
call_new_helper()



