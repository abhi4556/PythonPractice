import time
import logging
from functools import wraps

def decorate_logger(original_func):
    logging.basicConfig(filename='{}.log'.format(original_func.__name__),level=logging.INFO)
    @wraps(original_func)
    def wrapper_fun(*args, **kwargs):
        logging.info('Ran with args {}, and kwargs {}'.format(args,kwargs))
        return original_func(*args, **kwargs)
    return wrapper_fun
    

def decorate_timer(original_func):
    @wraps(original_func)
    def wrapper_fun(*args,**kwargs):
        t1 = time.time()
        original_func(*args,**kwargs)
        t2 = time.time()
        print ("Total time taken to execute {} {}".format((original_func.__name__),(t2-t1)))
        
        
    return wrapper_fun

@decorate_logger
@decorate_timer
def display_info(name,age):
    time.sleep(1)
    print ("Name is {} and age {}".format(name,age))
'''    
Issue with below code is once my decorate_timer is executed the diplay_info is holding the refernece to wrapper_fun
So when at line decorate_logger is called its basically passing the wrapper_fun hence the log created will be with name of wrapper_fun
Expected is the log name should be the name of display_info 

display_info = decorate_timer(display_info)  -> It calls the decorate_timer and in return get wrapper_fun
display_info("Abhi","37")  -> Calls wrapper_fun which internally calls display_info at line 14. Here original_fun is basically referiing to display_info 

display_info = decorate_logger(display_info)
display_info("Abhijit", "38")
'''
#How to avoid above issue
#use inbuild functools which remember the original func means one more level of decorating

# display_info = decorate_timer(display_info) 
# display_info("Abhi","37")  

# display_info = decorate_logger(display_info)
# display_info("Abhijit", "38")

display_info("abhi",'32')

