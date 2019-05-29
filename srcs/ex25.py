'''In English, the present participle is formed by adding the suffix
-ing to the infinite form: go -> going.
A simple set of heuristic rules can be given as follows:
If the verb ends in e, drop the e and add ing
(if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant,
double the final letter before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form()
which given a verb in infinitive form returns its present participle form.
Test your function with words such as lie, see, move and hug.
However, you must not expect such simple rules to work for all cases.'''

from ex04 import is_vowel

def make_ing_form(v):
	'''
	This function takes a verb in infinitive form and returns its
	present participle form

	Parameters
	----------
	v (string): a verb in infinitive form

	Returns
	----------
	verb in its present participle form
	'''
	#if not isinstance(v, str):
	#	raise TypeError('This function requires a string.')
	
	exceptions = ('be', 'see', 'flee', 'knee')
	if v.endswith('ie'):
		return v[:-2] + 'ying'
	elif v.endswith('e') and v not in exceptions:
		return v[:-1] + 'ing'
	#elif not is_vowel(v[-3]) and is_vowel(v[-2]) and not is_vowel(v[-1]):
	#	return v + v[-1] + 'es'
	return v + 'ing'

print(make_ing_form('flee'))
print(make_ing_form('lie'))
print(make_ing_form('do'))
print(make_ing_form('fly'))
print(make_ing_form('bruise'))
print(make_ing_form('add'))