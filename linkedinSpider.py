from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy import log
from congruence.items import CongruenceItem
from os import path
from congruence.parser.HtmlParser import HtmlParser
import os
import urllib
import json
from bs4 import UnicodeDammit
from congruence.db import MongoDBClient

class linkedinSpider(CrawlSpider):
          name = "linkedin"
          allowed_domains = "www.linkedin.com"
          jsonFile = open('items.json', 'r')
	  j_list = json.load(jsonFile)
	  i=0
          k=0
          done_urls = []
          for entity in j_list['profiles']:
              done_urls.append(j_list['profiles'][k]['url'])
              k = k + 1
	  start_urls = []
          k = 0
          for entity in j_list['profiles']:
              if 'also_view' in j_list['profiles'][k]:
                 for criteria in j_list['profiles'][k]['also_view']:
		     i = i + 1
	         for j in range( 0, i-1 ):
                     if j_list['profiles'][k]['also_view'][j]['linkedin_id'] in done_urls:
                        continue
                     else:
                        start_urls.append(j_list['profiles'][k]['also_view'][j]['linkedin_id'])
                        done_urls.append(j_list['profiles'][k]['also_view'][j]['linkedin_id'])
              else:
                 done_urls.append(j_list['profiles'][k]['url'])   
              k=k+1
              i = 0

          def parse(self, response):
                 response = response.replace(url=HtmlParser.remove_url_parameter(response.url))
                 hxs = HtmlXPathSelector(response)
                 personProfile = HtmlParser.extract_person_profile(hxs)
                 linkedin_id = self.get_linkedin_id(response.url)
                 linkedin_id = UnicodeDammit(urllib.unquote_plus(linkedin_id)).markup
                 if linkedin_id:
                  personProfile['_id'] = linkedin_id
                  personProfile['url'] = UnicodeDammit(response.url).markup
                  yield personProfile
          
          def get_linkedin_id(self, url):
             find_index = url.find("linkedin.com/")
             if find_index >= 0:
                return url[find_index + 13:].replace('/', '-')
             return None       
 
