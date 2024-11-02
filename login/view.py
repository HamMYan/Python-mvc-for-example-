def get_login_credentials()->dict:
    """This view will get user credentials to login 
    to the system
    """
    info = {}
    info["email"] = input("Enter your email: ")
    info["password"] = input("Enter your password: ")
    return info