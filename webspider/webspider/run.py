from spiders.shanghairanking import ShanghairankingSpider
from spiders.dmoz_spider import DmozSpider

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import json
import xlwt

json_file = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_shanghairanking_v2.json")
config_rules = json.load(json_file)

# open Workbook
workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)

settings = Settings()

# crawl settings
#settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
#settings.set("ITEM_PIPELINES" , {
#    'pipelines.DuplicatesPipeline': 200,
#    # 'pipelines.CountDropPipline': 100,
#    'pipelines.DataBasePipeline': 300,
#})

process = CrawlerProcess(settings)

print "process"
print process
print "type(process):"
print type(process)


for ranking_name in config_rules:
    print ranking_name
    worksheet = workbook.add_sheet(ranking_name)
    process.crawl(ShanghairankingSpider, config_rules[ranking_name], worksheet)
    

print "process.start() here ..."
process.start() # the script will block here until the crawling is finished

# save workboot
print "before save workbook ..."
workbook.save("ShanghaiRanking.xls")
print "after save workbook ..."

