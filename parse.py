import pymongo
from pymongo import Connection
connection = Connection()
db = connection['test_database']
collection = db['test_collection']
post = {"name": "Mike",
         "text": "studied in pesit and worked on c",
         "tags": ["c++", "python", "java"],
	 "c++": 0,
	 "c":0,
	 "java":0,"recommender":"John"},{"name": "John",
         "text": "studied cse and worked on java",
         "tags": ["eclipse", "c", "java"],
	 "c++":0,
	 "c":0,
	 "java":1,"recommender":"tulip"},{"name": "Luke",
         "text": "studied ece and worked on c and java",
         "tags": ["c", "java"],
	 "c++": 0,
	 "c":4,
	 "java":3,"recommender":"Mike"}
posts = db.posts
posts.insert(post)
find_skills = posts.find_one({"name": "Mike"})
line=find_skills['text']
words = line.split() 
skills = ["c++","c","java"]
for current_word in words:
    if current_word in skills:
	a = posts.find_one({"name": "Mike"}) 
	a[current_word] = 2
	recommender_name = a['recommender']
	rec = posts.find_one({"name": recommender_name})
	if rec[current_word] > 2 :
	  a[current_word] = 3
	posts.save(a)
print(posts.find_one({"name": "Mike"}))
	
