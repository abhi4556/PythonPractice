#!/usr/bin/python
num_list = [1 , 2, 3, 4, 5, 6, 7, 8, 9]
#           0 , 1, 2, 3, 4, 5, 6, 7, 8
#           -9,-8,-7,-6,-5,-4,-3,-2,-1       

#Note for any slicing first create a indexing chart in your brain 
#if both start and end point are positive make sure you are traversing from left to right
#if both the start and end point are negative make sure you are traversion from left to right
#
#list[x:y:x]  x-> starting point  y-> ending but not inclusive  z-> step(jump)
print(num_list[1:9]) 

print(num_list[-7:-1])  
#o/p [3, 4, 5, 6, 7, 8]

print(num_list[-1:-7])
#o/p as -1 to -7 

#Reverse
print(num_list[-1::-1])

print(num_list[2:3])

'''
Certainly! Let's delve deeper into the concept of slicing direction and its alignment with the order of indices.

In Python, when you use slicing with a step value, the direction of the slicing is determined by the sign of the step value.

If the step value is positive, the slicing moves from the starting index towards the stopping index in the forward direction.
If the step value is negative, the slicing moves from the starting index towards the stopping index in the reverse direction.
To ensure that the slicing direction aligns with the order of the indices, the starting index needs to be greater than the stopping index when the step value is negative.

Here's an example to illustrate this concept:

python
Copy code
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_list[2:7:1])  # Slicing from index 2 to index 7 with a step of 1 (forward direction)
In this example, the starting index is 2, the stopping index is 7, and the step value is 1. Since the step value is positive and the starting index is smaller than the stopping index, the slicing direction is aligned with the order of the indices, and the resulting slice is [3, 4, 5, 6, 7].

Now, let's consider a scenario where the step value is negative and the starting index is greater than the stopping index:

python
Copy code
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_list[7:2:-1])  # Slicing from index 7 to index 2 with a step of -1 (reverse direction)
In this case, the starting index is 7, the stopping index is 2, and the step value is -1. Since the step value is negative and the starting index is greater than the stopping index, the slicing direction is aligned with the order of the indices, and the resulting slice is [8, 7, 6, 5, 4, 3].
'''

#Note You need to maintain the direction
# [7:4] Here the direction is right to left (<-) and by default step index is (1) and direction of step index is left to right hence it doesnt fit
# and the o/p is none
#[7:4:-1] Here the direction is right to left (<-) and  step index is (-1) and also direction of step index is right  to left.
#Hence it will give o/p

#Let's say l = [1,2,3,4] where length = 4. Now when I tried printing l[-10:23] (where both ends are greater than length), it was printing out the entire list. why so? should it give index error?
#In Python, when you perform list slicing, if the specified indices are outside the valid range of the list, instead of raising an IndexError, Python will adjust the indices to the valid range and return the corresponding slice. This behavior is designed to be more forgiving and flexible.