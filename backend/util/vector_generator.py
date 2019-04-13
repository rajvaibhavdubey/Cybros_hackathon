from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

class Vector_generator:
	'''
		Is responsible for generating vectors in the form of dictonaries
		for all the provided translations
	'''

	def __init__( self, language='english' ):
		self.lemmatizer = WordNetLemmatizer()
		self.stop_words = set( stopwords.words( language ) ) 

	def vectorize( self, translation_list ):
		'''
			takes a list of sentences and converts them to a list of vectors
		'''
		vector_list = []
		for translation in translation_list:
			temporary_list = self.tokenize( translation.lower() )
			temporary_dict = {}
			for key in temporary_list:
				if key in temporary_dict.keys():
					temporary_dict[key] = temporary_dict[key] + 1
				else:
					temporary_dict[key] = 1
			vector_list.append( temporary_dict )
		return vector_list

	def tokenize( self, sentence ):
		'''
			convert sentence to vector and remove stop words
		'''
		vector = word_tokenize( sentence )
		# vector = sentence.split()
		# filtered_vector = []
		# for term in vector:
			# root_term = self.lemmatizer.lemmatize(term)
			# root_term = term
			# if root_term not in self.stop_words: 
			# 	filtered_vector.append(root_term)
		# return filtered_vector
		return vector
