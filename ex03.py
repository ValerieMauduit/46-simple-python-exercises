'''Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself
is nevertheless a good exercise.)'''

def length(str):
    '''
    This function computes the length of a given list or string

    Parameters
    ----------
    str (list or string)

    Returns
    ----------
    The length (int)
    '''
    length = 0
    for i in str:
        length += 1
    return length

'''Uncomment the following lines to test the function and try to change the
string or the list passed to the length() function. Compare results with the
len() built in function.'''

# print('String length = {}'.format(length('Hello world!')))
# print('List length = {}'.format(length([0, 1, 2, 3, 4, 5])))
