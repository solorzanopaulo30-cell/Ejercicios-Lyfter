from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    def get_role(self):
        return "you are an admin"

    def has_permission(self, permission):
        return True


class RegularUser(User):
    def get_role(self):
        return "you are an user"

    def has_permission(self, permission):
        if permission == "read":
            return True
        else:
            return False

#-------------------------------
user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))
print(user2.has_permission("delete"))