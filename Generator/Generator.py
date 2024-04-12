#!/usr/bin/python
#generator: By using a yield keyword we can use generator
# Generator are better in performance
# Instead of returing entire list generator returns an object
# We can iterate over objec to fetch the data

#EX1 wap to generate a square of elemenet in a list
''''
def square_of_num(list_of_num):
    for num in list_of_num:
        yield (num*num)
        
list_of_num = [1,2,3,4]
list_of_num_obj = square_of_num(list_of_num)

for num in list_of_num_obj:
    print("Squared number is {}".format(num))
'''
#Generator comprehension
def generate_list_of_num():
    #list_of_num = []
    # for num in range(1,10):
    #     list_of_num.append(num)
    gen_num_obj = (num for num in range(1,10))
    return gen_num_obj

list_of_num_obj = (num*num for num in generate_list_of_num())
for num in list_of_num_obj:
    print("Squared number is {}".format(num))

