import json
jsonFile = open('items.json', 'r')
j_list = json.load(jsonFile)
i=0
for criteria in range(0,j_list['also_view'].length):
	i = i + 1
print i
 #   for key, value in criteria.iteritems():
#		print key
 #   print ''
