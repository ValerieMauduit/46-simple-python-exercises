'''Write a version of a palindrome recognizer that also accepts phrase
palindromes such as "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization,
and spacing are usually ignored.'''

def is_phrase_palindrome(str):
    '''
    This function recognizes palindromes and accepts phrase palindromes
    (i.e. words that look the same written backwards)
    Punctuation, capitalization, and spacing are usually ignored

    Parameters
    ----------
    str (string)

    Returns
    ----------
    True if the phrase is a palindrome
    False otherwise
    '''
    phrase = [i.lower() for i in str if i.isalpha()]
    return phrase == phrase[::-1]
