# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_deudores project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_deudores'

SPIDER_MODULES = ['scrapy_deudores.spiders']
NEWSPIDER_MODULE = 'scrapy_deudores.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_deudores (+http://www.yourdomain.com)'

HTTP_PROXY = "http://127.0.0.1:8123"

DOWNLOADER_MIDDLEWARES = {
        'scrapy_deudores.middlewares.ProxyMiddleware': 410,
}

