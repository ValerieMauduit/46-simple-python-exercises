'''Write a function translate() that will translate a text into "rövarspråket"
(Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string
"tothohisos isos fofunon".'''

from string import ascii_letters

def translate(txt):
    '''
    This function translates a given text into "robber's language"
    that is a swedish game where you double every consonant
    and place an occurrence of "o" in between

    Parameters
    ----------
    txt (string): the input text

    Returns
    ----------
    Translated text
    '''
    consonants = set(ascii_letters) - set('aeiouAEIOU')
    return ''.join([l+'o'+l if l in consonants else l for l in txt])
