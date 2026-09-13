#Acceso por clave, `.keys()`, `.items()`, diccionarios anidados.
#3. Cree una función que combine dos diccionarios en uno solo (si hay claves repetidas, sume los valores).


def unify_dictionaries(dict1, dict2):
    unified_dic = dict.copy()
    for key,value in dict2.items():
        if key in unified_dic:
            unified_dic[key] += value
        else:
            unified_dic[key] = value
    print(unified_dic)


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(unify_dictionaries(dict1, dict2))