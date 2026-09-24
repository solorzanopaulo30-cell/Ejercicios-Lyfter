#
#5. Cree una función que reciba otra función como argumento y la aplique a cada elemento de una lista (mini versión de `map`).


def mini_map(func, lst):
    return [func(x) for x in lst]

