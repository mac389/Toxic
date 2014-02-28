import cPickle
import brewer2mpl

import numpy as np
import visualization.Graphics as artist
from visualization.visualization import SemanticVisualization as SV

from prettyplotlib import plt
from prettyplotlib import mpl

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from matplotlib import rcParams

rcParams['text.usetex'] = True

data = np.memmap('/Volumes/My Book/Toxic/data/alcohol.similarity-matrix-tsv',
				dtype='float32',mode='r',shape=(469,469))

sanitized = np.tril(data.copy())
sanitized += sanitized.transpose()
sanitized *= 0.5

sanitized[np.isnan(sanitized)] = 1
mask = np.tri(sanitized.shape[0],k=-1).transpose()
masked = np.ma.array(sanitized,mask=mask)

'''
fig,axs = plt.subplots(nrows=1,ncols=2)
cmap = plt.cm.get_cmap('jet_r',50)
cmap.set_bad('w')
cax = axs[1].imshow(masked,interpolation='nearest',aspect='auto', cmap = cmap)
plt.colorbar(cax)


axs[0].hist(sanitized.ravel(),bins=100,color='k')

map(artist.adjust_spines,axs)
axs[0].set_ylabel(artist.format('Frequency'))
axs[0].set_xlabel(artist.format('Semantic Distance'))

axs[1].set_ylabel(artist.format('Tweet'))
axs[1].set_xlabel(artist.format('Tweet'))
plt.tight_layout()
plt.show()
'''
pca =PCA(n_components=2)
pca.fit(sanitized)

decomp = plt.figure()
panel = decomp.add_subplot(111)
panel.scatter(pca.components_[0,:]*np.sqrt(pca.explained_variance_ratio_[0]), 
				pca.components_[1,:]*np.sqrt(pca.explained_variance_ratio_[1]),s=20,c='k')
artist.adjust_spines(panel)
panel.set_xlabel(r'\Large $\mathbf{1^{st}}$ \textbf{Semantic Dimension}')
panel.set_ylabel(r'\Large $\mathbf{2^{nd}}$ \textbf{Semantic Dimension}')
plt.show()

'''
x = SV('')
x.frequencies(open('../data/alcohol.txt','rb').read().replace('\n',''))
'''