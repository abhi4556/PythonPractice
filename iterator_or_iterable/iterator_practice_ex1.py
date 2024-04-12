#!/usr/bin/python
''' coding problem for iterator and iterable'''

class Sentence:
    def __init__(self,start):
        self.start =  start
        self.my_list = self.start.split()
        self.counter = 0
        

    def __iter__(self):
        return self

    def __next__(self):
        index_val = len(self.my_list)
        if self.counter >= index_val:
            raise StopIteration()
        val = self.my_list[index_val - (index_val - self.counter )]
        self.counter += 1
        return val



my_sentence = Sentence('This is a test')
for word in my_sentence:
    print(word)

'''
write a generator 
it return a iterator
'''
def sentences(msg):
    for word in msg.split():
        yield word

words = sentences("I am good")
for w in words:
    print(w)