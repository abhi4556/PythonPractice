#!/usr/bin/python
'''

Certainly! Here are some questions to test your understanding of list comprehension in Python:

1. How can you create a new list that contains the squared values of the numbers from 1 to 10 using list comprehension?
2. Given a list of integers, how can you use list comprehension to create a new list that contains only the even numbers from the original list?
3. How can you use list comprehension to transform a list of strings into a new list where each string is capitalized?
4. Given two lists of numbers of the same length, how can you use list comprehension to create a new list that contains the element-wise sum of the two lists?
5. How can you use list comprehension to filter out all the negative numbers from a list of integers?

Feel free to try solving these questions, and I'll be here to help you if you need any assistance or explanations!
'''

# EX1

squared_value = [x*x for x in range(1,11) ]
print(squared_value)

#EX 2
list_of_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_no = [x for x in list_of_num if x%2 == 0]
print(even_no)

#EX 3
list_of_string = ['abhi', 'raja', 'ritu']
upper_case_string = [word.upper() for word in list_of_string]
print(upper_case_string)

#Ex 4
list_of_num1 = [1,2,3,4]
list_of_num2 = [5,6,7,8]
new_list = [(list_of_num1[index] + list_of_num2[index]) for index in range(0,len(list_of_num1))]
print(new_list)

#Ex 5
list_of_number = [-1,2,3,-4,-5]
list_of_negative_num = [x for x in list_of_number if x < 0]
print(list_of_negative_num)