# Flipkart-Price-Tracker
Application which take the root url of the E-store and extracts useful information like name,price,url,rating etc of the products available, and store it in a database.


### Design
The crawler is created using Scrapy and BeautifulSoup.
#### Working of the crawler:
1. This crawler is for Flipkart.com
2. The spider (spider/test.py) takes start URL to begin crawling and then crawls flipkart.com according to given rules.
3. The response received from the webpage is parsed using BeautifulSoup to get the product's name, description, price, rating, number of reviews, data and time of retrieval. The functions used for this purpose are written in the file `spiders/appdefs.py` which is imported in the `spiders/test.py` file.
4. Then all the product details are inserted into the database through pipeline `pipelines.py` using python-MySQLdb.

#### Rules for crawler:
1. Only domain name 'flipkart.com' is allowed.
2. 2 seconds delay after every request.
3. Depth limit is set to 10.
4. Redirect of URL is disabled to avoid problems in crawling.

#### How to Run
#####  Steps to deploy the crawler:
1. In the `config.py` file:
    1. Change the server address, username, password and database name.
    2. If xampp is used, set the value of SERVERXAMPP to True, else False.
2. Command to run the crawler:
    1. Goto the MyApp folder.
    2. Command: scrapy crawl MyApp

#### Frontend:

It is made using Html and PHP to view the data stored in database.

##### Steps to deploy the website which shows the product information:
1. Copy the 'website' folder and paste it in '/var/www/' folder.
2. In 'connection.php', change the username and password.
3. Import the csl_assignment.sql file. This will create a database with name "csl_assignment".
4. Open `http://localhost/index.php` in browser along with path of the folder.

#### Updating the existing the database 
**To be executed daily via scheduler such as crontab**

1. 'update/update.py' file should be run to update the database.
2. It fetches all the URLs from the database, parses the response from these pages and adds a new entry for each product in the database.

##### How to run:
1. In the `config.py` file:
    1. Change the server address, username, password and database name.
    2. If xampp is used, set the value of SERVERXAMPP to True, else False.
2. Execute `update.py` file present in the 'update' folder.

