# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from config import *

class MyappPipeline(object):
    def process_item(self, item, spider):

		print item

		if (SERVERXAMPP):
			db = MySQLdb.connect(SERVER,USERNAME,PASSWORD,DATABASE,unix_socket=XAMPP)
		else:
			db = MySQLdb.connect(SERVER,USERNAME,PASSWORD,DATABASE)
		print "Connection established to database"

		cursor = db.cursor()

		try:
			#SQL query to insert
			cursor.execute('''INSERT INTO records (product_name,description,price,rating,num_review,product_url,date,time)
							  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''',
							  (item['name'],item['description'],item['price'],item['rating'],item['usersrated'],item['url'],item['date'],item['time']))
			print "Insert Successful"
		except Exception,e:
			print str(e)

		db.commit()
		db.close()
        
