import pymongo
from pymongo import Connection
connection = Connection()
db = connection['some_database']
collection = db['some_collection']
post = {"name": "Mike",
         "education": "IIT Bombay",
         "degree": "M.Tech","subject":"computer science","profile_index" : 0.0},{"name": "John",
         "education": "PESIT",
         "degree": "B.E",
	 "subject":"electronics","profile_index" : 0.0},{"name": "Luke",
         "education": "MSRIT","degree":"B.Tech",
         "subject": "mechanical","profile_index" : 0.0}
posts = db.posts
posts.insert(post)
top_indian = ["IIT Bombay","NIT","RVCE","PESIT"]
ug_degree = ["B.E","B.C.A","B.C.S","BSc","B.Tech"]
pg_degree = ["M.S","M.C.A","M.C.S","MSc","M.Tech"]
rank_1 = 5
rank_2 = 2
docs = posts.find()
print [records for records in docs]
for record in docs:
  find_entity = posts.find_one({"_id": record['_id']})
  if find_entity['education'] in top_indian:
	find_entity['profile_index'] += 0.2*rank_1
  else:
	find_entity['profile_index'] += 0.2*rank_2
  posts.save(find_entity)
check = posts.find()
print "after the changes"
print [check_changes for check_changes in check]
	


