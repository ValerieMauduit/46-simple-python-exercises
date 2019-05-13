'''Write a function filter_long_words() that takes a list of words and
an integer n and returns the list of words that are longer than n.'''

from ex03 import length

def filter_long_words(lst, n):
    '''
    This function filters a list of words and returns them if longer than n

    Parameters
    ----------
    lst (list of strings)
    n (int)

    Returns
    ----------
    The list of words that are longer than n (list of strings)
    '''
    return [w for w in lst if length(w) > n]
