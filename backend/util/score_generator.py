import math
from vector_generator import Vector_generator
from tsne import Graph_generator


class Score_generator:
	def __init__( self, translation_threshold=10 ):
		self.translation_threshold = translation_threshold
		self.vector_generator = Vector_generator( )
		self.graph_generator = Graph_generator()

	def score( self, translation_list ):
		'''
			takes a list of translations and return a score between 0 and 1,
			a score greated than 0.8 means a fit to use translation
		'''
		normalized_vector_list = self.normalize( self.vector_generator.vectorize( translation_list ) )
		vector_space = self.vector_space_generator( normalized_vector_list )
		
		mean_vector = self.find_mean( normalized_vector_list, vector_space )
		normalized_mean_vector = self.normalize( [ mean_vector ] )[0]
		standard_deviation = self.find_standard_deviation( normalized_mean_vector, normalized_vector_list )
		distance_list = self.distance_list_generator( normalized_mean_vector, normalized_vector_list )

		scores = self.rating_function( distance_list, standard_deviation, self.translation_threshold )
		scored_translation_list = []
		for index, score in enumerate( scores ):
			scored_translation_list.append( { translation_list[ index ] : score } )

		tsne_output = self.graph_generator.reduce_dims( normalized_vector_list, normalized_mean_vector )
		max_score = 0
		best_fit = ''
		for element in scored_translation_list:
			if max_score < element.values()[0]:
				max_score = element.values()[0]
				best_fit = element.keys()
			else:
				continue
		print tsne_output 
		print best_fit
		print 1 - standard_deviation

	def vector_space_generator( self, normalized_vector_list ):
		vector_space = []
		for vector in normalized_vector_list:
			for element, value in vector.iteritems():
				if element not in vector_space:
					vector_space.append( element )
		return vector_space
		

	def normalize( self, vector_list ):
		'''
			normalizes the list of vectors
		'''
		normalized_vector_list = []
		for vector in vector_list:
			normalized_vector = {}
			sum = 0
			for element, value in vector.iteritems():
				sum += ( value ** 2 )
			sum = math.sqrt( sum )
			for element, value in vector.iteritems():
				normalized_vector[ element ] = vector[ element ] / sum
			normalized_vector_list.append( normalized_vector )
		return normalized_vector_list

	def distance_list_generator( self, mean_vector, normalized_vector_list ):
		distance_list = []
		for vector in normalized_vector_list:
			distance_list.append( self.distance( mean_vector, vector ) )
		return distance_list

	def distance( self, mean_vector, vector ):
		distance = 0
		for element in mean_vector.keys():
			if element in vector.keys():
				distance += math.pow( mean_vector[ element ] - vector[ element ], 2 )
			else:
				distance += math.pow( mean_vector[ element ], 2 )
		distance = math.sqrt( distance )
		return distance

	def rating_function( self, distance_list, standard_deviation, translation_threshold ):
		'''
			Gives a score value based on three metrics -
			distance of each vector from mean vector
			standard deviation of the whole distribution
			translation threshold
		'''
		scored_list = []
		for element in distance_list:
			scored_list.append( (1 / element) )
		return scored_list

	def find_mean( self, normalized_vector_list, vector_space ):
		'''
			takes a vector space and normalized vector list
			returns a means vector in the form of dictonary
		'''
		number_of_vectors = len( vector_space )
		mean_vector = {}
		for element in vector_space:
			mean_vector[ element ] = 0
		for element in vector_space:
			for vector in normalized_vector_list:
				if element in vector.keys():
					mean_vector[ element ] += vector[ element ]
				else:
					continue
			mean_vector[ element ] /= number_of_vectors
		return mean_vector

	def find_standard_deviation( self, mean_vector, normalized_vector_list ):
		sum = 0
		for vector in normalized_vector_list:
			sum += math.pow( self.distance( mean_vector, vector ), 2 )
		return math.sqrt( sum / ( len( normalized_vector_list ) ) )