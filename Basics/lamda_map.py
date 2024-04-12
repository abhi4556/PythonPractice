#!/usr/bin/python
#use lamda function
# syntax lambda argument:expression
#argument can be more but expression should be one
num=[1,2,3,4]
#print(list(lambda x,x*x))

#map function
# function: sequence
print(list(map(lambda x:x*x,num)))

num1=[1,2,3,4]
num2=[5,6,7,8]
print(list(map((lambda x,y:x+y),num1,num2)))


#filter function
# function,iteratable
# must be only one iterable
number1=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2==0,number1)))

#reduce function
# function, iterables
# must be only one iterable
import functools
print(functools.reduce(lambda x,y:x+y ,number1))