import cPickle


import numpy as np
import visualization.Graphics as artist
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


from matplotlib import rcParams

rcParams['text.usetex'] = True

data = np.memmap('/Volumes/My Book/Toxic/data/alcohol_shor.similarity-matrix-tsv',
				dtype='float32',mode='r',shape=(200,200))

sanitized = data.copy()
sanitized[np.isnan(sanitized)] = 1

fig,axs = plt.subplots(nrows=1,ncols=2)

cax = axs[1].imshow(sanitized,interpolation='nearest',aspect='auto', cmap = plt.cm.jet_r)
plt.colorbar(cax)


axs[0].hist(sanitized.ravel(),bins=100,color='k')

map(artist.adjust_spines,axs)
axs[0].set_ylabel(artist.format('Frequency'))
axs[0].set_xlabel(artist.format('Semantic Distance'))

axs[1].set_ylabel(artist.format('Tweet'))
axs[1].set_xlabel(artist.format('Tweet'))
plt.tight_layout()
plt.show()