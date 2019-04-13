"""Write a function char_freq() that takes a string and builds a frequency
listing of the characters contained in it. Represent the frequency listing as a
Python dictionary.
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab")."""

def char_freq(str):
    '''
    This function takes a string and builds a frequency listing
    of the characters contained in it

    Parameters
    ----------
    str (string)

    Returns
    ----------
    The listing as a Python dictionary
    '''
    listing = {}
    for c in str:
        if c in listing:
            listing[c] += 1
        else:
            listing[c] = 1
    return listing

'''Uncomment the following line to test the function and try to change the
string passed to the char_freq() function.'''

# print(char_freq("abbabcbdbabdbdbabababcbcbab"))
# print(char_freq("abracadabra"))
