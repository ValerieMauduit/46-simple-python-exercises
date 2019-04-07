'''Write a function is_member() that takes a value (i.e. a number, string, etc)
x and a list of values a, and returns True if x is a member of a,
False otherwise.
(Note that this is exactly what the in operator does, but for the sake of the
exercise you should pretend Python did not have this operator.)'''

def is_member(x, a):
    '''
    This function checks if a value x is a member of a list of values a

    Parameters
    ----------
    x (string, int, float): a value
    a (list): a list of values

    Returns
    ----------
    True if x is in the list a
    False otherwise
    '''
    return x in a


'''Uncomment the following lines to test the function and try to change the
value and the list passed to the is_member() function.'''

# print(is_member('a', [0, 1, 2, 3, 4, 5]))
# print(is_member(1, [0, 1, 2, 3, 4, 5]))
# print(is_member('a', [0, 1, 2, 'a', 'b', 5]))
# print(is_member(4.2, [4, 2, 42, 4.2]))
# print(is_member('hello', ['hello world', 42]))
# print(is_member('hello', ['hello', 'world']))
