import nltk
from nltk import pos_tag,word_tokenize
from nltk.corpus import wordnet as wn

""" synsets = wn.synsets("good")
print [str(syns.definition) for syns in synsets]
"""
sentence1 = "Proven ability to define and implement strategies that improve internal organization, bridge IT and business organizations, and client services. Very good in c++. Additional expertise reducing costs and increasing revenue streams, and ERP and outsource relationship management. Instrumental in achieving significant cost reductions and value chain improvements through re-engineering, team building, and providing leadership holding significant and diverse roles across the United States, Asia and Europe"
adj = []
good = ["good","estimable","beneficial","practiced","effective","efficient"]
expert = ["excellent", "first-class", "fantabulous", "splendid","substantially","advantageously","skillful", "skilful","best","proficient","expert","amazing"]
average = ["trivial","little","minuscule","little extent","less","minimal","minimum","lower limit","average","fair"]
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
A = 2

tokenized_sent = word_tokenize(sentence1)
for word in tokenized_sent:
  if word.lower() in nltk.corpus.stopwords.words('english'):
  continue
  else:
	tag_tuples = nltk.pos_tag(word)
        for (string, tag) in tag_tuples:
                token = {'word':string, 'pos':tag}
		if tag.startswith('JJ') or tag.startswith('RB') :
			   adj.append(word)
for ad in adj:
  if ad in good:
	num_3 += 1
  elif ad in average:
	num_1 += 1
  elif ad in expert:
	num_5 += 1
  else :
	synonyms = []
	for i, syn in enumerate(wn.synsets(ad, pos='a')):
          syns = [n.replace('_', ' ') for n in syn.lemma_names]
	  synonyms.append(syns)
	for c in synonyms:
	  if c in good:
	     num_3 += 1
  	  elif c in average:
	     num_1 += 1
  	  elif c in expert:
	     num_5 += 1
	  else:
	     num_2 += 1 
	

adjective_weight = (1*num_1+2*num_2+3*num_3+4*num_4+5*num_5+A*3)/(num_1+num_2+num_3+num_4+num_5+A)
print(adjective_weight)

  
	
