#!/usr/bin/python
#Write a code to see how much memory a list consumes and compare using implementing same code using generator

#create a  1 million dictionary using random data
#import mem_profile
import random
import time

#Note in python3 we dont have xrange and we only have range which return a generator object
#python 2 range exist which returns a list and xrange return a generator


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

#print 'Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil())

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.time()
# people = people_list(1000000)
# t2 = time.time()

t1 = time.time()
people = people_generator(1000000)
t2 = time.time()

#print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
import sys
print("Memory {}".format(sys.getsizeof(people)))
print ('Took {} Seconds'.format(t2-t1))

'''
Output difference of list and generator in term of size. Basically list holds the entire data in memory
and generator only holds the generator object in memory

PS C:\My_Project\Support_files\Python_practice\Generator> python .\GeneratorEx2.py
Memory 8448728
Took 1.3773338794708252 Seconds

PS C:\My_Project\Support_files\Python_practice\Generator> python .\GeneratorEx2.py
Memory 104
Took 0.0 Seconds

'''

