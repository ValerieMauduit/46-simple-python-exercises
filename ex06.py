'''Define a function sum() and a function multiply()
that sums and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10,
and multiply([1, 2, 3, 4]) should return 24.'''

def sum(nbrs):
    '''
    This function sums all the numbers in a list of numbers

    Parameters
    ----------
    nbrs (list): a list of numbers

    Returns
    ----------
    The sum of the elements of the list
    '''
    res = 0
    for i in nbrs:
        res += i
    return res

def multiply(nbrs):
    '''
    This function multiplies all the numbers in a list of numbers

    Parameters
    ----------
    nbrs (list): a list of numbers

    Returns
    ----------
    The multiplication of the elements of the list
    '''
    res = 1
    for i in nbrs:
        res *= i
    return res

'''Uncomment the following line to test the function and try to change the list
of numbers passed to the sum() and the multiply() functions.
To test the function sum(), change its name (e.g., sum1() or sum2()) as a sum()
function already exists.'''

# print('Sum = {}'.format(sum([1, 2, 3, 4])))
# print('Multiply = {}'.format(multiply([1, 2, 3, 4])))
