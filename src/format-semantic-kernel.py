from __future__ import unicode_literals

import os,json,string,re
from nltk import word_tokenize
from nltk.corpus import stopwords


trigger = '#-'
READ = 'rb'
WRITE ='wb'
base = '/Volumes/My Book'
filenames = [filename for filename in os.listdir('/Volumes/My Book') if trigger in filename]
my_stopwords = [word.rstrip('\r\n').encode('utf-8') for word in open('../data/stopwords',READ).readlines()]
punctuation = set(string.punctuation) #Can make more efficient with a translator table


def cleanse(tweet):
	#This ignores emoticons, replace word_tokenize with a better regex
	tokens = [word.encode('ascii').lower() for word in word_tokenize(tweet) if all([ord(symbol)<128 for symbol in word])]
	tokens = [token for token in tokens 
				if not any([token in verboten 
								for verboten in [my_stopwords,punctuation,['rt','http'],stopwords.words('english')]])
				and not token.isdigit()]
	tokens = [word for word in tokens if not word.isdigit() and word is not 't']
	tokens = re.findall(r'\w+',' '.join(tokens))
	return ' '.join(list(set(tokens)))
	'''
	return ' '.join([word.lower() for word in word_tokenize(tweet) 
				if not any([word in verboten for verboten in [my_stopwords,punctuation,['RT','http','HTTP'],stopwords.words('english')]])
				and all([ord(symbol)<128 and symbol not in punctuation and not symbol.isdigit() for symbol in word])])
	'''
text = [' '.join([cleanse(tweet['text']) 
			for tweet in json.load(open(os.path.join(base,filename),READ))]) 
			for filename in filenames[:1]][0]
print len(text)
with open('db-text',WRITE) as f:
	print>>f,text
	
#	f.write([cleanse(tweet['text']) for tweet in json.load(open(os.path.join(base,filename),READ)) for filename in filenames])

