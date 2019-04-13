import numpy as np
from sklearn.manifold import TSNE

class Graph_generator:
	def reduce_dims( self, normalized_vector_list, normalized_mean_vector ):
		key_index = []
		vector_list = []
		for key in normalized_mean_vector.keys():
			key_index.append( key )
		for vector in normalized_vector_list:
			temp_vector = [] 
			for element in key_index:
				if element in vector.keys():
					temp_vector.append( vector[ element ] )
				else:
					temp_vector.append( 0 )
			vector_list.append( temp_vector )
		X = np.array( vector_list, dtype = float )
		X_embedded = TSNE(n_components=2).fit_transform(X)
		return X_embedded