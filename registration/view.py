def gather_user_info_view() -> dict:
    """this view will gather user information
    (i.e. First Name, Last Name, email address
    and password)
    """
    info = {}
    info["name"] = input("Enter your name: ")
    info["surname"] = input("Enter your surname: ")
    info["email"] = input("Enter your email: ")
    info["password"] = input("Enter your password: ")
    return info