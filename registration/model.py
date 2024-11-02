def save_user_in_db(user_info: dict) -> bool:
    """_summary_

    Args:
        user_info (dict): user info (i.e. name, surname, email and pass)

    Returns:
        bool: True if save was successful
    """
    sql = f"""
    INSERT INTO users_table (name,surname,email,password)
    VALUES ({user_info['name'],user_info['surname'],user_info['email'],user_info['password']})
    """
    print(sql)
    return True
