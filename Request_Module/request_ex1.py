#/usr/bin/python
import requests

#Request Module is good for getting information from website but to parse them you can use beautiful soop or simailar packages
payload = {'page':2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
#We can directly paas the parameter in the url but it prone to error
#So always advaisable to pass the parametre as a disctionar and call it as payload or any other name
# printing the url give all the details
#
print(r.text)
print(r.url)



#r = requests.get('https://httpbin.org/get', params=payload)
payload = {'username': 'abhi', 'password' : 'test123'}
r = requests.get('https://httpbin.org/post', data=payload)
r_dict = r.json() # we get the response to post method as a json. We have a way to store json response in a dictionary
print(r_dict['form'])

#Authetication using url
r = requests.get('https://httpbin.org/basic-auth/abhi/test123', auth=('abhi','test123'),timeout = 3)
print(r.text)