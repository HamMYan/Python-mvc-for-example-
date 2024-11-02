from .view import get_login_credentials
from .model import validate_credentials


def login_user():
    """This controller will handle user login.
    It will gather user credentials from the login view
    and validate them against the database.
    """
    print("==== Login to the system ====")
    user_info = get_login_credentials()
    result = validate_credentials(user_info)

    print("Login Successfull")