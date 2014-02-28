import nltk, string

import numpy as np
import matplotlib.pyplot as plt
import Graphics as artist

from matplotlib import rcParams

rcParams['text.usetex'] = True
exclude = set(string.punctuation)

format = lambda text: r'\textbf{%s}'%text
READ = 'rb'
stopwords = [word.rstrip('\r\n').strip() for word in open('/Users/michaelchary/Toxic/data/stopwords',READ).readlines()]
emoticons = [word.rstrip('\r\n').strip() for word in open('/Users/michaelchary/Toxic/data/emoticons',READ).readlines()]

class SemanticVisualization(object):

	def __init__(self,trigger, delimiter = '\t'):
		self.trigger = trigger
		self.filename = '/Volumes/My Book/Toxic/data/%s.similarity-matrix-tsv'%(trigger)
		#again with the dangerous path constructions	
		self.delimiter = delimiter

		#self.data = np.loadtxt(self.filename,delimiter=self.delimiter, dtype='str')

	def heatmap(self,ax=None, show=False,savename=None):

		if not ax:
			fig = plt.figure()
			ax = fig.add_subplot(111)

		cax = ax.imshow(self.data,interpolation='nearest',aspect='auto')
		ax.set_ylabel(r'\Large \textbf{Comment}')
		ax.set_xlabel(r'\Large \textbf{Comment}')
		ax.set_title(r'\Large \textbf{Similarity of tweets about %s}'%self.trigger)
		plt.colorbar(cax)
		plt.tight_layout()
		if savename:
			plt.savefig('%.png'%savename,dpi=200)
		if show:
			plt.show()

	def frequencies(self,str, ax=None, cutoff=30):
		words = nltk.word_tokenize(''.join(ch for ch in str 
											if ch not in exclude 
												and ord(ch)<128 
												and not ch.isdigit()).lower())
		words = [word for word in words if word not in stopwords 
										and word not in emoticons 
										and word  not in ['rt','amp']]
		fdist = nltk.FreqDist(words)
		freqs = fdist.items()[:cutoff]
		word,f =zip(*freqs)
		f = np.array(f).astype(float)
		f /= float(f.sum())
		if not ax:
			fig = plt.figure()
			ax = fig.add_subplot(111)

		ax.plot(f,'k',linewidth=2)
		artist.adjust_spines(ax)
		ax.yaxis.grid()
		ax.xaxis.grid()
		ax.set_xticks(range(len(word)))
		ax.set_xticklabels(map(format,word),range(len(word)), rotation=90)
		ax.set_ylabel(r'\Large $\log \left(\mathbf{Frequency}\right)$')
		plt.tight_layout()
		plt.show()