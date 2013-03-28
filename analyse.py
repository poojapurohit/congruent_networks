import pymongo
import json
from pymongo import MongoClient
connection = MongoClient()
db = connection['cong']
person = db.profile
d = open("data.dat")
f = json.load(d)
i = 0
for entity in person.find():
     for key in f["values"][i]:
         person.update({"name":entity['name']},{"$set": {key:f["values"][i][key]}})
     i=i+1

  
    
