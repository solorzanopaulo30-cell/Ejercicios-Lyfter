from datetime import datetime

def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_str = ", ".join(str(a) for a in args)
        timestamp = datetime.now()
        print(f"func:{func.__name__} - args: {args_str} - [{timestamp}] - Result: {result}")
        return result
    return wrapper


def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"the argument {arg!r} is not a nomber.")
        return func(*args, **kwargs)
    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a * b


multiply(3, 4)