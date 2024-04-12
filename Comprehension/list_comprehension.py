#/usr/bin/python
nums = [1, 2, 3, 4, 5]

new_nums = [n for n in nums]
print(new_nums)

new_nums = [n*n for n in nums]
print(new_nums)


even_nums = [n for n in nums if n%2 == 0]
print(even_nums)

# input (a,b,c,d) and (0123)
num = [0, 1, 2, 3]
alpha = ['a', 'b', 'c', 'd']
new_list = [(n,a) for n in num for a in alpha ]
print(new_list)