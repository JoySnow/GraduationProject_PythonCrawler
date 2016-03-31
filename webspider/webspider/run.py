from spiders.shanghairanking import ShanghairankingSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json

#json_file = file("./config_shanghairanking.json")
json_file = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_shanghairanking_v2.json")
config_rules = json.load(json_file)

process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
#process.crawl('', domain='scrapinghub.com')


for ranking_name in config_rules:
    print ranking_name
    new_spider = ShanghairankingSpider(config_rules[ranking_name])
    process.crawl(new_spider)

process.start() # the script will block here until the crawling is finished

