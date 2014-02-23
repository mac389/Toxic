import json
import itertools

from time import time
from pprint import pprint
from src.nlp.SemanticString import SemanticString
from nltk.corpus import wordnet
from termcolor import colored 

filename = './data/semantic-distance-database.json'
READ = 'rb'
WRITE = 'wb'
APPEND = 'a+'

#strings = ["I like dogs :-)","I like rum.","I like drinking.", "I like pot."]
strings = ["I smoke pot :-).","I like rum."]
start = time()



print('/----------------Beginning test ------------\\')

for one in strings:
	for two in strings:

		print '---'
		d1 = SemanticString(one,{})
		d2 = SemanticString(two,{})

		print '|%s|'%(repr(d1))
		print '|%s|'%(repr(d2))

		print '|Semantic distance: %.04f |'%(d1-d2)
		print '---'
print '---'
print '|Duration %.04f s|'%(time()-start)
print('\----------------Finished test ------------/')

