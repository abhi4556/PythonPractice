import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'(https?:)//(www\.)?(\w+)(\.\w+)')

#subbed_urls = pattern.sub(r'\2\3', urls)

#print(subbed_urls)

matches = pattern.finditer(urls)
#matches = pattern.findall(urls) It gives the matched pattern without any additional info as what we get as part of finditer
#matches = pattern.search(urls)  It doesnt return the iterator but gives the match sequence if found else none
#matches = pattern.match(urls) #only checks at beginging of string 
for match in matches:
    print(match.group(2))
    print(match)