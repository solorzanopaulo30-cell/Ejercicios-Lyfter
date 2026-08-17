

user_logged_in = False


def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise Exception("User not verified")
        return func(*args, **kwargs)
    return wrapper


@requires_login
def view_profile():
    print("Showing user profile")


try:
    view_profile()
except Exception as e:
    print(f"Error: {e}")