import pymongo
from pymongo import Connection
connection = Connection()
db = connection['profile_data']
posts = db.posts
docs = posts.find()
top_indian = ["IIT Bombay","NIT","RVCE","PESIT"]
ug_degree = ["B.E","B.C.A","B.C.S","BSc","B.Tech","Engineering"]
pg_degree = ["M.S","M.C.A","M.C.S","MSc","M.Tech"]
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
i = 0
j = 0
A = 2
tier = ["Project Manager","Senior Proejct Manager","location manager","account manager","resource manager","delivery manager","President","VP","Vice President","Chief Operating Officer","COO","Director","Chief Technology Officer","CTO"]
for record in docs:
  find_entity = posts.find_one({"_id": record['_id']})
  if find_entity['education'][i]['name'] in top_indian:
  num_4 += 1
  else:
	num_2 += 1
  if find_entity['education'][i]['degree'] in ug_degree:
	num_3 += 1
  elif find_entity['education'][i]['degree'] in pg_degree:
	num_4 += 1
  else:
	num_1 += 1
  for criteria in find_entity['experience']:
		j = j + 1
  for k in range( 0, j-1 ):
	if find_entity['experience'][k]['title'] in tier:
		num_5 +=1
	else:
		num_3 +=1

 
  find_entity['profile_index']=(1*num_1+2*num_2+3*num_3+4*num_4+5*num_5+A*3)/(num_1+num_2+num_3+num_4+num_5+A)			
  posts.save(find_entity)
  

check = posts.find()
print "after the changes"
print [check_changes['profile_index'] for check_changes in check]
	

