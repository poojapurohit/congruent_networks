import difflib

likes={
    "rajat":["music","x-men","programming","hindi","english","himesh","lil wayne","rap","travelling","coding"],
    "steve":["travelling","pop","hanging out","friends","facebook","tv","skating","religion","english","chocolate"],
    "toby":["programming","pop","rap","gardens","flowers","birthday","tv","summer","youtube","eminem"],
    "ravi":["skating","opera","sony","apple","iphone","music","winter","mango shake","heart","microsoft"],
    "katy":["music","pics","guitar","glamour","paris","fun","lip sticks","cute guys","rap","winter"],
    "paul":["office","women","dress","casuals","action movies","fun","public speaking","microsoft","developer"],
    "sheila":["heart","beach","summer","laptops","youtube","movies","hindi","english","cute guys","love"],
    "saif":["women","beach","laptops","movies","himesh","world","earth","rap","fun","eminem"],
    "mark":["pilgrimage","programming","house","world","books","country music","bob","tom hanks","beauty","tigers"],
    "stuart":["rap","smart girls","music","wrestling","brock lesnar","country music","public speaking","women","coding","iphone"],
    "grover":["skating","mountaineering","racing","athletics","sports","adidas","nike","women","apple","pop"],
    "anita":["heart","sunidhi","hindi","love","love songs","cooking","adidas","beach","travelling","flowers"],
    "kelly":["travelling","comedy","tv","facebook","youtube","cooking","horror","movies","dublin","animals"],
    "dino":["women","games","xbox","x-men","assassin's creed","pop","rap","opera","need for speed","jeans"],
    "priya":["heart","mountaineering","sky diving","sony","apple","pop","perfumes","luxury","eminem","lil wayne"],
    "brenda":["cute guys","xbox","shower","beach","summer","english","french","country music","office","birds"]
}
for key in likes:
    print 'rajat', key, difflib.SequenceMatcher(None,likes['rajat'],likes[key]).ratio()
