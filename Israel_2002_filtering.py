import json 

with open('Israel_2002.json', encoding='utf8') as file:  
    data = json.load(file)
print(data)