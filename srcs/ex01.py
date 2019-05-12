'''Define a function max() that takes two numbers as arguments and returns the
largest of them. Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it yourself
is nevertheless a good exercise.)'''

def mymax(n1, n2):
    '''
    This function takes two numbers as arguments and returns the largest of them

    Parameters
    ----------
    n1 (int or float): first number
    n2 (int or float): second number

    Returns
    ----------
    The largest of the two numbers
    '''
    if n1 > n2:
        return n1
    else:
        return n2