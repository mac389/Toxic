def princomp(A,numpc=0):
 # computing eigenvalues and eigenvectors of covariance matrix
 M = (A-mean(A.T,axis=1)).T # subtract the mean (along columns)
 [latent,coeff] = linalg.eig(cov(M))
 p = size(coeff,axis=1)
 idx = argsort(latent) # sorting the eigenvalues
 idx = idx[::-1]       # in ascending order
 # sorting eigenvectors according to the sorted eigenvalues
 coeff = coeff[:,idx]
 latent = latent[idx] # sorting eigenvalues
 if numpc < p and numpc >= 0:
  coeff = coeff[:,range(numpc)] # cutting some PCs if needed
 score = dot(coeff.T,M) # projection of the data in the new space
 return coeff,score,latent