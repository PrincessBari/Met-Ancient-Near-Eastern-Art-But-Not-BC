import glob
import json
import re

bc_pattern = re.compile(r'[B|b]+\.*[C|c]+')

has_dimensions = 0

for filename in glob.glob('data/*.json'):
	with open(filename, 'r') as jsonfile:
		data = json.load(jsonfile)

		bc_search = bc_pattern.search(data['objectDate'])
		
		if bc_search == None:
			
			print(data['title'], data['objectID'], data['objectBeginDate'])
			

	
			