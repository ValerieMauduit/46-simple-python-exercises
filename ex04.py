'''Write a function that takes a character (i.e. a string of length 1)
and returns True if it is a vowel, False otherwise.'''

def is_vowel(char):
    '''
    This function recognizes vowels
    y can be added in the vowel list if necessary

    Parameters
    ----------
    char (string of length 1): a character

    Returns
    ----------
    True if the character is a vowel
    False otherwise
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    return char.lower() in vowels

'''Uncomment the following lines to test the function and try to change the
string of size 1 passed to the is_vowel() function. You can also add y to the
vowel list.'''

# print(is_vowel('a'))
# print(is_vowel('b'))
