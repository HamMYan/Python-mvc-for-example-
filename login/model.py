def validate_credentials(user_info:dict)->bool:
    """
    This function checks if user credentials exist in the database.

    Args:
        user_info (dict): User information (i.e., email and password).

    Returns:
        bool: True if credentials exist, False otherwise.
    """
    sql = f'''
    SELECT * FROM users_table
    WHERE email='{user_info['email']} AND password='{user_info['password']}'
    '''
    print(sql)
    return True