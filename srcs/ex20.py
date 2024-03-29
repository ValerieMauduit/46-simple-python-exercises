'''Represent a small bilingual lexicon as a Python dictionary in the following
fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"år"} and use it to translate your Christmas cards from
English into Swedish. That is, write a function translate() that takes a list of
English words and returns a list of Swedish words.'''

def translate(lst):
	'''
	This function translates English words into Swedish words

	Parameters
	----------
	lst (list of strings)

	Returns
	----------
	Translated list
	'''
	xmas_dict = {
		'merry': 'god',
		'christmas': 'jul',
		'and': 'och',
		'happy': 'gott',
		'new': 'nytt',
		'year': 'år'
		}
	return [xmas_dict[w.lower()] for w in lst]
