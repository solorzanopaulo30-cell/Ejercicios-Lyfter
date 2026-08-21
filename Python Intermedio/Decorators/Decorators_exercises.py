

#first exercise
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Parámetros: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Retorno: {result}")
        return result
    return wrapper

#second exercise 
def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"El argumento {arg!r} no es un número.")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"El argumento '{key}'={value!r} no es un número.")
        return func(*args, **kwargs)
    return wrapper


@log_decorator
@validate_numbers
def add(a, b):
    return a + b


add(3, 5)