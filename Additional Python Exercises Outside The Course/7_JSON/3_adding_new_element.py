#`json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`.
#3. Cree una función que agregue un nuevo elemento a una lista guardada en un archivo JSON.


import json


def add_element(filename,new_element):
    with open(filename,"r") as file:
        data = json.load(file)
    data.append(new_element)
    with open(filename,"w") as file:
        json.dump(data,file)
    return data
