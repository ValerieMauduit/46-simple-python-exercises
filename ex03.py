"""Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself
is nevertheless a good exercise.)"""

def length(str):
    """
    This function computes the length a given list or string

    Parameters
    ----------
    a list or a string

    Returns
    ----------
    The length (int)
    """
    length = 0
    for i in str:
        length += 1
    return length
