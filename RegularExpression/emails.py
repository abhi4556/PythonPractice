import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

#pattern = re.compile(r'(C|c)orey(M|\.|-\d{3}-)[Ss][a-z]{6}@[a-z]+(-)?[a-z]+\.[a-z]{3}')
pattern = re.compile(r'([a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net))')

matches = pattern.finditer(emails)

for match in matches:
    print(match.group())