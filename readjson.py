import json
d = open("items.json")
f = json.load(d)
i = 0
for entity in f["profiles"]:
   print f["profiles"][i]["name"]
   i = i + 1
    
