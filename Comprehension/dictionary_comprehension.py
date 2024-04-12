#!/usr/bin/python
first_name = ['abhi', 'raja', 'pari']
last_name = ['mukherjee', 'mukherjee', 'khangar']

dict_of_name = {name:title for name,title in zip(first_name,last_name)}
print(dict_of_name)