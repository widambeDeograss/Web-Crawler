import scrapy
from scrapy.utils.sitemap import Sitemap
import json
import requests
from urllib.parse import urlparse
from scraper import trendDetection

trendDetection.check_trends()

# data = []
# print("Started Reading JSON file which contains multiple JSON document")
# with open('scraper/links.jl') as f:
#     for jsonObj in f:
#         urlDict = json.loads(jsonObj)
#         data.append(urlDict)
#
# print("Printing each JSON Decoded Object")
# for url in data:
#     sr = "'" + url["url"] + "'"
#     print(type(sr))
#     print(sr)
#     break
#
url = "https://www.bbc.com/robots.txt"
part = urlparse(url)
href = part.netloc

print(href)

# crawling by using sitemaps


# class SitemapJustUrlsSpider(scrapy.Spider):
#     name = "sitemap_spider"
#     start_urls = (
#         'http://www.example.com/sitemap.xml',
#     )
#
#     def parse(self, response, **kwargs):
#         score = Sitemap(response.body)
#         for sitelink in score:
#             url = sitelink['loc']
#             yield {'url': url}

# data = []
# with open('scraper/updatedL.jl', 'r', encoding="utf-8") as f:
#     for urlDict in f:
#         url = json.loads(urlDict)
#         data.append(url)
#
# for obj in data:
#     print(obj["url"])
#     break

