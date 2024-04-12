#!/usr/bin/python
list_of_file =  [{u'content': u"request platform software system shell\r\n\r\n\r\nvmcloud netcreate --virl /home/laasadmin/abhimukh/taas_code/scripts/cat9k/cat9k_virl_EX1.virl --topology abhi_demo_ex1\r\nvmcloud netcreate --virl /home/laasadmin/abhimukh/taas_code/scripts/cat9k/cat9k_virl_EX2.virl --topology abhi_demo_ex2\r\nvmcloud netcreate --virl /home/laasadmin/abhimukh/taas_code/scripts/cat9k/cat9k_virl_EX3.virl --topology abhi's_demo_ex3\r\n", u'name': u'demo_Zach.txt'}, {u'content': u'request platform software system shell\r\n\r\n\r\nvmcloud netcreate --virl /home/laasadmin/abhimukh/taas_code/scripts/cat9k/cat9k_virl_EX1.virl --topology abhi_demo_ex1\r\nvmcloud netcreate --virl /home/laasadmin/abhimukh/taas_code/scripts/cat9k/cat9k_virl_EX2.virl --topology abhi_demo_ex2\r\nvmcloud netcreate --virl /home/laasadmin/abhimukh/taas_code/scripts/cat9k/cat9k_virl_EX3.virl --topology abhi_demo_ex3\r\n', u'name': u'Zach.txt'}]
my_str= []
new_dict = {}
temp = ""
flag = False
for data in list_of_file:
    #print(data.items())
    for (key,value) in sorted(data.items()):
        #print("Name {} and content {}".format(key,value))
        if (key == 'content'):
            temp = value
            continue
        if (key == 'name'):
            #count = count
            new_dict[value] = temp

#s = pickle.dumps(new_dict)
#print("Converted to str %s" %s)
#d = pickle.loads(s)
import json
import ast
#import yaml
test = "test"
#d=json.dumps(test)
falg = True
#back_to_dict = json.loads(test)
#print("From str to dict %s" %back_to_dict)
        
        #my_str.append(''.join(value))
        #if (value == "")
        #my_str.append("***********")

#print(my_str)
#d = ast.literal_eval(test)
# display d and its type
try:
    d = json.loads(test)
except Exception:
    flag = False
    print("Error caught")

if(flag):
    print("In if")
elif flag == False:
    print("In else if")
else:
    print("In else")