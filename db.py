import pymongo
from pymongo import Connection
connection = Connection()
db = connection['profile_data']
collection = db['profile_collection']
post = {"education": [{"major": "Electronics(Electrical)", "end": "1992", "name": "University of Mumbai", "degree": "Engineering", "start": "1988", "desc": ""}], "group": {"affilition": ["CIO Advisory Group", "CIO Forum", "CIO Leadership Board", "Forbes CIO Network", "RAIT Alumni Network"]}, "name": {"family_name": "Naik", "given_name": "Ravi"}, "locality": "San Francisco Bay Area", "url": "http://www.linkedin.com/pub/ravi-naik/1/7a4/aa8", "industry": "Information Technology and Services", "experience": [{"org": "SanDisk", "end": "Present", "start": "June 2012", "title": "CIO &amp; 'VP WW Facilities'"}, {"org": "SanDisk", "start": "September 2009", "title": "Vice President &amp; CIO"}, {"org": "SanDisk", "start": "October 2007", "title": "IT ERP Director"}, {"org": "Hewlett Packard", "start": "January 2007", "title": "IT Director"}, {"org": "Mercury Interactive", "start": "November 2005", "title": "ERP Director"}, {"org": "3Com Corporation", "desc": "Diverse experience in IT strategy, enterprise program execution, planning, and operations management. Proven ability to define and implement strategies that improve internal organization, bridge IT and business organizations, and client services. Additional expertise reducing costs and increasing revenue streams, and ERP and outsource relationship management. Instrumental in achieving significant cost reductions and value chain improvements through re-engineering, team building, and providing leadership holding significant and diverse roles across the United States, Asia and Europe.", "start": "December 1997", "title": "ERP Manager"}, {"org": "Hewlett Packard", "desc": "Technical consultant to Hewlett Packard TMO, member of the SAP Development team.", "start": "July 1994", "title": "Senior SAP Consultant"}], "also_view": [{"url": "in-sumitsadana", "linkedin_id": "http://www.linkedin.com/in/sumitsadana"}, {"url": "in-prabreddy", "linkedin_id": "http://www.linkedin.com/in/prabreddy"}, {"url": "pub-vikram-pamarthi-1-458-2a6", "linkedin_id": "http://www.linkedin.com/pub/vikram-pamarthi/1/458/2a6"}, {"url": "pub-gursharan-singh-a-ab7-254", "linkedin_id": "http://cn.linkedin.com/pub/gursharan-singh/a/ab7/254"}, {"url": "pub-tomer-mekhty-4-295-28a", "linkedin_id": "http://www.linkedin.com/pub/tomer-mekhty/4/295/28a"}, {"url": "pub-sanjay-mehrotra-4-800-350", "linkedin_id": "http://www.linkedin.com/pub/sanjay-mehrotra/4/800/350"}, {"url": "pub-cecilia-claudio-3-62b-50a", "linkedin_id": "http://www.linkedin.com/pub/cecilia-claudio/3/62b/50a"}, {"url": "pub-manish-bhatia-28-5a2-868", "linkedin_id": "http://www.linkedin.com/pub/manish-bhatia/28/5a2/868"}, {"url": "pub-judy-bruner-18-b49-163", "linkedin_id": "http://www.linkedin.com/pub/judy-bruner/18/b49/163"}], "_id": "pub-ravi-naik-1-7a4-aa8"} 

posts = db.posts
posts.insert(post)