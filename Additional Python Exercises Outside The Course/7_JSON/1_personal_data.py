#`json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`.
#1. Cree un programa que guarde un diccionario con datos personales en un archivo JSON.


import json


personal_date = {
    "name":"Paolo Maldini",
    "age":"25",
    "profesion":"Football player"
}

with open ("personal_data.json","w") as file:
    json.dump(personal_date,file)
    