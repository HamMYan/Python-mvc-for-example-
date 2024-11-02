from .view import gather_user_info_view
from .model import save_user_in_db


def register_user() -> None:
    """
    This controller will handle user registration
    It will gather user info from regstration view
    and will save gathered info in database
    """
    print("====Registration====")
    user_info = gather_user_info_view()
    result = save_user_in_db(user_info)

    print("Registration completed")