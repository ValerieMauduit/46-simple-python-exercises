"""Define a function is_palindrome() that recognizes palindromes
(i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True."""

def is_palindrome(w):
    """
    This function recognizes palindromes
    (i.e. words that look the same written backwards)

    Parameters
    ----------
    w (string): a word

    Returns
    ----------
    True if the word is a palindrome
    False otherwise
    """
    return w == w[::-1]
