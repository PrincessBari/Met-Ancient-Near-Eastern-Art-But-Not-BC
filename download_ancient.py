# this stopped after 4520/6221
# I didn't have much time so worked with what I had

import requests
import json 

r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=3')

objects = json.loads(r.text)
objects = objects['objectIDs']

counter = 0
for object_id in objects:

	obj_r = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}')
	
	try:
		obj_data = json.loads(obj_r.text)

		with open(f'data/{object_id}.json', 'w') as out:
			json.dump(obj_data, out, indent=2)
	
	except:
		print(f'Something went wrong with {object_id}')

	counter+=1

	print(f"{counter}/{len(objects)}")

print(len(objects))