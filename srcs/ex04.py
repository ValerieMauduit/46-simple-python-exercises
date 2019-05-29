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
	if len(char) > 1:
		raise ValueError('This function requires a character (string of size 1).')
	return char.lower() in vowels
