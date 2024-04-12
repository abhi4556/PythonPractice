#/usr/bin/python
''' Create a classs which will act as builting range function'''

class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end
        print("Constructor called")

            
    def __iter__(self):
        print("Iter function called")
        return self

    def __next__(self):
        print("Next method called")
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value+= 1
        return current

nums = MyRange(1,5)  # it only calls constructor
for num in nums:
    print(num)
    print(nums)
#print(next(nums)) 
