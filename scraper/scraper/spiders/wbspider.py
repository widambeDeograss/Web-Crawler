import json
from abc import ABC
from scrapy import Spider, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from time import sleep
from bs4 import BeautifulSoup
import requests
from scrapy.spiders import SitemapSpider
import redis

# extract links from a list of seed urls
"""
"https://millardayo.com/", "https://www.mwananchi.co.tz/", "https://www.ippmedia.com/sw/nipashe",
"https://tz.linkedin.com/", "https://www.researchgate.net/", "https://swahilitimes.co.tz/",
"https://www.bbc.com/swahili/","https://dailynews.co.tz/", "https://bongo5.com/", "https://globalpublishers.co.tz/",
"https://mtanzania.co.tz/", "https://habarileo.co.tz/", "https://www.thecitizen.co.tz/tanzania", "https://www.tanzania.go.tz/"
"""


class WebSpider(Spider):
    name = "web"
    allowed_domains = ['mabumbe.com']
    start_urls = ["https://mabumbe.com/"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.link_extractor = LinkExtractor(unique=True, attrs='href')

    def parse(self, response, **kwargs):
        for link in self.link_extractor.extract_links(response):
            if link.url is not None:
                yield {
                    'url': link.url
                }
                yield response.follow(link.url, callback=self.parse)


class PageContent(Spider, ABC):
    name = 'page_content'

    def start_requests(self):
        urlList = []
        with open('updated2L.jl') as f:
            for jsonObj in f:
                urlDict = json.loads(jsonObj)
                urlList.append(urlDict)

        newList = list({v['url']: v for v in urlList}.values())  # removing redundant urls
        for url in newList:
            sleep(1)
            yield Request(url["url"], self.parse_urls)

    # extract page content from the urls list
    def parse_urls(self, response):
        # part = urlparse(response.url)
        # href = part.netloc + part.path + "post.html"
        # href = href.split('/')[-2]
        # with open(f'htmlPages/{href}.html', 'ab', encoding='utf-8') as f:
        #     f.write(response.body)
        try:
            yield {
                'url': response.url,
                'title': json.dumps(response.css('title::text').get(), ensure_ascii=False),
                'description': json.dumps(response.xpath("//meta[@name='description']/@content").get(),
                                          ensure_ascii=False),
                'keywords': json.dumps(response.xpath("//meta[@name='keywords']/@content").get(), ensure_ascii=False)
            }
        except:
            yield {
                'url': response.url,
                'title': json.dumps(response.css('title::text').get(), ensure_ascii=False),
                'description': '',
                'keywords': ''
            }


class ImageExtractor(Spider, ABC):
    name = 'image'

    def start_requests(self):
        urlList = []
        with open('updated2L.jl') as f:
            for jsonObj in f:
                urlDict = json.loads(jsonObj)
                urlList.append(urlDict)

        newList = list({v['url']: v for v in urlList}.values())  # removing redundant urls
        for url in newList:
            sleep(1)
            yield Request(url["url"], self.parse_urls)

    # extract page content from the urls list
    def parse_urls(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        images = soup.find_all('img')
        for image in images:
            try:
                yield {
                    'url': response.url,
                    'keywords': json.dumps(image["alt"], ensure_ascii=False),
                    'image': response.urljoin(image["src"])
                }
            except:
                yield {
                    'url': response.url,
                    'keywords': '',
                    'image': response.urljoin(image["src"])
                }


class PdfExtractor(Spider, ABC):
    name = "pdf"

    def start_requests(self):
        # "https://codex.cs.yale.edu/avi/os-book/OS9/practice-exer-dir/index.html"
        urlList = []
        with open('updated2L.jl') as f:
            for jsonObj in f:
                urlDict = json.loads(jsonObj)
                urlList.append(urlDict)

        newList = list({v['url']: v for v in urlList}.values())  # removing redundant urls
        for url in newList:
            sleep(1)
            yield Request(url["url"], self.parse_)

    def parse_(self, response):
        for href in response.css('a::attr(href)').extract():
            if href.endswith('.pdf'):
                sleep(1)
                yield Request(
                    url=response.urljoin(href),
                    callback=self.save_pdf
                )

    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        yield {
            "pdfTerm": path,
            "pdfUrl": response.url
        }
        self.logger.info('Saving PDF %score', path)
        with open(f'pdfFiles/{path}', 'ab') as f:
            f.write(response.body)


class HtmlParser(Spider, ABC):
    name = "body"

    def start_requests(self):
        urlList = []
        with open('updated2L.jl') as f:
            try:
                for jsonObj in f:
                    if jsonObj is not None:
                        urlDict = json.loads(jsonObj)
                        urlList.append(urlDict)
            except json.JSONDecodeError as e:
                print(e.msg, e)

        newList = list({v['url']: v for v in urlList}.values())  # removing redundant urls
        for url in newList:
            sleep(1)
            yield Request(url["url"], self.parse_urls)

    # extract page content from the urls list
    def parse_urls(self, response):
        # sleep(1)
        urlHTML = requests.get(response.url)
        soup = BeautifulSoup(urlHTML.text, 'html.parser')
        value = soup.get_text().strip()

        try:
            yield {
                'url': response.url,
                'words': json.dumps(value.split(), ensure_ascii=False)
            }
        except:
            print('keywords extraction failure')


class SiteSpider(SitemapSpider, ABC):
    r = redis.Redis()
    name = 'SiteSpider'
    allowed_domains = ["bbc.com"]
    # 'https://www.bbc.com/sitemaps/https-index-com-news.xml'
    # 'https://www.bbc.com/sitemaps/https-sitemap-com-news-1.xml'
    sitemap_urls = ['https://www.bbc.com/robots.txt']

    # sitemap_rules = [
    #     ('.*.xml', 'parse_sitemap')
    # ]

    # sitemap_follow = ['.*.xml', '.*.xml.gz']

    # other_urls = ['http://www.example.com/about']

    def sitemap_filter(self, entries):
        for entry in entries:
            # date_time = datetime.strptime(entry['lastmod'], '%Y-%m-%dT%H:%M:%S%z')
            # if date_time.year <= 2022:
            if not self.r.sismember('links', entry['loc']):
                url = entry['loc']
                self.r.sadd('links', url)
                yield entry
                with open('sitemapUrl.jl', 'a') as f:
                    json.dump(entry, f, ensure_ascii=False)
                    f.write('\n')
            else:
                continue

    # def start_requests(self):
    #     request = list(super(SiteSpider, self).start_requests())
    #     request += [Request(x, self.parse_other) for x in self.other_urls]
    #     return request

    def parse(self, response, **kwargs):
        print('This is the response', response.url)


# execution outside a project
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(WebSpider)
    process.crawl(PageContent)
    process.crawl(ImageExtractor)
    process.crawl(PdfExtractor)
    process.crawl(HtmlParser)
    process.start()
