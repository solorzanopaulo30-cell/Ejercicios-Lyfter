from datetime import date
from functools import wraps


class User:
    def __init__(self, name, date_of_birth):
        self._name = name
        self._date_of_birth = date_of_birth

    @property
    def name(self):
        return self._name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self._date_of_birth.year
        if (today.month, today.day) < (self._date_of_birth.month, self._date_of_birth.day):
            age -= 1
        return age


def require_adult(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError(f"{user.name} es menor de edad ({user.age} años).")
        return func(user, *args, **kwargs)
    return wrapper


@require_adult
def buy_alcohol(user):
    return f"{user.name} puede comprar alcohol."


# --------------------------

user1 = User("Carlos", date(1990, 5, 20))
user2 = User("Andrea", date(2015, 3, 10))

try:
    print(buy_alcohol(user2))
except ValueError as e:
    print(f"No se pudo completar la acción: {e}")