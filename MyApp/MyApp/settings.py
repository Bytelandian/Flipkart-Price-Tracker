# -*- coding: utf-8 -*-

# Scrapy settings for MyApp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'MyApp'

DOWNLOAD_DELAY = 2

SPIDER_MODULES = ['MyApp.spiders']
NEWSPIDER_MODULE = 'MyApp.spiders'
#LOG_LEVEL='ERROR'
DEPTH_LIMIT = 10
REDIRECT_ENABLED=False

ITEM_PIPELINES = {
        'MyApp.pipelines.MyappPipeline': 1,
    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MyApp (+http://www.yourdomain.com)'
