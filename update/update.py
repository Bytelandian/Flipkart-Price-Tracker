import MySQLdb
from config import *
import urllib2
from appdefs import *
import bs4
from datetime import datetime
import time

def getItem(f,url):
	item= {}
	soup=bs4.BeautifulSoup(f)
	item['url'] = url
	if '&' in item['url']:
		item['url']=item['url'].split('?')[0]
	item['name'] = getName(soup)
	item['description'] = getDescription(soup)
	item['price'] = getPrice(soup)
	[item['rating'],item['usersrated']]=getRating(soup)
	[item['date'],item['time']] = (str(datetime.now())).split()
	item['time']=item['time'].split('.')[0]
	return item

if (SERVERXAMPP):
	db = MySQLdb.connect(SERVER,USERNAME,PASSWORD,DATABASE,unix_socket=XAMPP)
else:
	db = MySQLdb.connect(SERVER,USERNAME,PASSWORD,DATABASE)
print "Connection Made"

cursor = db.cursor()

try:
	cursor.execute('''SELECT * FROM records ''')
	print "query Successful"
	for x in cursor:
		print x[3]
		link=urllib2.urlopen(x[3])
		res=link.read()
		item=getItem(res,x[3])
		cursor.execute('''INSERT INTO records (product_name,description,price,rating,num_review,product_url,date,time)
							  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''',
							  (item['name'],item['description'],item['price'],item['rating'],item['usersrated'],item['url'],item['date'],item['time']))

		print "INSERT Successful"
		time.sleep(5)

except Exception,e:
	print str(e)
db.commit()
db.close()
