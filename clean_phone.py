import pandas as pd

def validate_phone(phone_number):
    """ Ensure that the phone numbers are valid

    Arguments:
    phone_number - A Pandas Series of phone number as string objects

    Returns:
    A boolen Pandas Series.  True means it's valid.
    """
    return True


print(validate_phone(True))