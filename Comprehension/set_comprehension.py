#!/usr/bin/python
list_of_num = [1,2,3,4,1,2,6,7]
#using {} we are using set comprehension
new_list = {num for num in list_of_num}
print(new_list)