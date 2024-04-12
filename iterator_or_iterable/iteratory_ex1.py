#/usr/bin/python
#what is a iterable
#Something where we can loop over is called as iterable e.g list,tuple,dict etc

#How can we say if something is iterable
#An object which has a attribute as __iter__ then its called as iterable

num = [1, 2, 3, 4]
#print(dir(num)) 
#if we run __iter__ on a list it will return an iterator. Iterator is an object with a state where it rememberes where its stay during iteration
#list is an iterable as it doesnt have a state and it doesnt know how to iterate over next value


#iterator also know how to get the next value for which it uses another dunder method called next

#when we run an __iter__ on a list it return a iterator

#iterator are also iterable
#iterator can only go forward

i_nums = num.__iter__() # its same as iter(nums)
print(dir(i_nums))
print(next(i_nums))
print(next(i_nums)) #it shows i_nums object remeber its state where it was last
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))

#practical example as why we need an iterator
