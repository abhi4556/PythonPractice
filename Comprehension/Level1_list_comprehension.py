#!/usr/bin/python
'''
Certainly! Here are some more challenging questions to test your understanding of list comprehension:

1. Given a list of strings, how can you use list comprehension to create a new list that contains only the strings with a length greater than 5?
2. How can you use list comprehension to create a new list that contains the factorial of each number from 1 to 10?
3. Given a list of words, how can you use list comprehension to create a new list that contains only the words that start with a vowel?
4. How can you use list comprehension to flatten a 2D list into a 1D list? For example, convert [[1, 2, 3], [4, 5, 6], [7, 8, 9]] into [1, 2, 3, 4, 5, 6, 7, 8, 9].
5. Given a list of numbers, how can you use list comprehension to create a new list that contains only the prime numbers from the original list?

Feel free to give them a try, and I'll be here to help you if you need any assistance or explanations!
'''
#EX1
list_of_str = ['abhi', 'abhijit', 'raja', 'I am good']
new_list_str = [word for word in list_of_str if len(word) > 5]
print(new_list_str)

#EX2
def factorial(num):
    result = 1
    for element in range(1,num+1):
        result = result * element
    return result

list_of_num = [factorial(num) for num in range(1,11)]
print(list_of_num)

#EX3
list_of_word = ['abhi', 'raja', 'ice','enemy','owl']
word_with_vowel = [word for word in list_of_word if word[0] in ['a','e','i','o','u']]
print(word_with_vowel)

#EX4

list_of_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
list_of_2d = [lst_elem for sub_list in list_of_2d for lst_elem in sub_list ]
print(list_of_2d)

#ex5
def isPrime(num):
    i=0
    if num%1 == 0 and num%num == 0:
        print("inside if")
        for fact in range(2,int(num/2)+1):
            print (fact)
            if num%fact != 0:
                return True
list_of_numbers = [8]
prime_list = [elem for elem in list_of_numbers if(isPrime(elem))]
print(prime_list)
    
        