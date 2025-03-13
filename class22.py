# import json

# data = {
#     "name": "Nasim Khan",
#     "age": 25,
#     "city": "Dhaka",
#     "skills": ["Python", "Django", "Machine Learning"]
# }

# json_data = json.dumps(data, indent=4)

# output = json.loads(json_data)

# print(type(output))

import re
# regEx


# text = "Hello123world2bye"
# patt = r'\d+'

# match = re.split(patt,text)

# print(match)

patt = r"^([a-z]+[0-9]*@[a-z]+\.[a-z]+)$"
phone_patt = r"^(\+?8?8?01[3-9][0-9]{8})$"

phone = ['asm124@gmail.com','123asm@gmail.net','asm@yahoo.net']

for num in phone:
    match = re.match(patt,num)
    if match:
        print('Valid: ',num)
    else:
        print('invalid: ',num)
