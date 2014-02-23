import json

import Graphics as artist
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['text.usetex'] = True

READ = 'rb'
kernels = json.load(open('../../data/normalized-semantic-kernel.json',READ))

#plot kernels that have more than three entries
cutoff = 3
ymin = 0
ymax = 1

format = lambda word: r'\Large \textbf{%s}'%''.join([ch for ch in word if ch not in ['-','_']])
#Iteritems returns a list of (key,value) tuples
for word,kernel in [item for item in kernels.iteritems() if len(item[1].values())>cutoff]:
	synonyms,weights = zip(*kernel.items())
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(weights,'.--',color='k', clip_on=False)
	artist.adjust_spines(ax)
	ax.set_ylim((ymin,ymax))
	ax.set_ylabel(format('Relative frequency'))
	ax.set_xlabel(format('Synonym'))
	ax.annotate(format(word), xy=(.2, .8),  xycoords='axes fraction',
                horizontalalignment='center', verticalalignment='center')

	ax.set_xticks(range(len(synonyms)))
	ax.set_xticklabels(map(format,synonyms),range(len(synonyms)),rotation=45)
	plt.tight_layout()
	plt.savefig('../../output/%s.png'%(word),dpi=300)