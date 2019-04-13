import sys, ast
from score_generator import Score_generator

score_generator = Score_generator()

list_of_translations = ast.literal_eval( sys.argv[1] )
score_generator.score( list_of_translations )