#!/usr/bin/python
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
890-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'


#raw string when we prefix a string with r it treats special character as raw string e.g
#\n it will consider as \n and not a new line

print("\n I am abhi")  #output :  I am abhi
print(r"\nI am abhi")  #output :  \nI am abhi

#re.compile  : It is used to compile a pattern and store it in variable so we can use the variable to search for the pattern
# [] : called as character set and we can pass any literal to it. 
#Note if we [^a-z] so carat here means negate so it matches other the a-z literal
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'M(r|s|rs)\.?\s[[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# with open('C:\My_Project\Support_files\Python_practice\RegularExpression\data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match )
 