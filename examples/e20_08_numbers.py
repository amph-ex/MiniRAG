import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
query=[[1.0,0.0]]
vectors=[[0.0,1.0],[1.0,0.0],[0.8,0.6]]
scores=cosine_similarity(query,vectors)[0]
indices=np.argsort(scores)[::-1][:2]
print(scores)
print(indices)
