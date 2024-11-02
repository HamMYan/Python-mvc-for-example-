from registration.controller import register_user
from login.controller import login_user


def start():
    """Starting point of the app
    """
    register_user()
    login_user()


if __name__ == "__main__":
    start()
