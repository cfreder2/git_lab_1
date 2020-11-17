import pandas as pd

def validate_phone(phone_number):
    """ Ensure that the phone numbers are valid

    Arguments:
    phone_number - A Pandas Series of phone number as string objects

    Returns:
    A boolen Pandas Series.  True means it's valid.
    """
    bool_mask = phone_number.str.contains(r"^\d{3}[-]?\d{3}[-]?\d{4}")
    return bool_mask


numbers = pd.Series(['342-123-5581','452-123-5979','12-10-1920'])
print(validate_phone(numbers))