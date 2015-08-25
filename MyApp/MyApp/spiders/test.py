from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector,Selector
import MyApp.items
import bs4
from datetime import datetime
from appdefs import *


class MySpider(CrawlSpider):
	#Name of the App
	name = "MyApp"

	#Allowed Domains to do scraping
	allowed_domains = ["flipkart.com"]

	#Start Urls of the applications
	start_urls=['http://www.flipkart.com/mobiles','http://www.flipkart.com/computers/laptops','http://www.flipkart.com/computers','http://www.flipkart.com/mens-clothing','http://www.flipkart.com/womens-clothing','http://www.flipkart.com/books','http://www.flipkart.com/home-store','http://www.flipkart.com/sports-fitness','http://www.flipkart.com/mens-footwear','http://www.flipkart.com/womens-footwear',"http://www.flipkart.com"]
	
	#Rules of the application
	rules = (
		Rule(SgmlLinkExtractor(allow=('/p/', ),deny=('/oauth2/','google.com','www.flipkart.com/reviews/',)),callback='parse_item'),
		Rule(SgmlLinkExtractor(allow=('flipkart.com', ),deny=('google.com','www.flipkart.com/reviews/',)),follow=True),
	)

	#Main Item to extract all details
	def parse_item(self, response):
		item= MyApp.items.MyappItem()
		f=response.body
		soup=bs4.BeautifulSoup(f)
		print response.url
		if ('/p/' in response.url):
			item['url'] = str(response.url)
			if '&' in item['url']:
				item['url']=item['url'].split('?')[0]
			item['name'] = getName(soup)
			item['description'] = getDescription(soup)
			item['price'] = getPrice(soup)
			[item['rating'],item['usersrated']]=getRating(soup)
			[item['date'],item['time']] = (str(datetime.now())).split()
			item['time']=item['time'].split('.')[0]
			return item