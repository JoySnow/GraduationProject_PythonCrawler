from spiders.shanghairanking import ShanghairankingSpider
from spiders.qsranking import QSrankingSpider
from spiders.webometricsranking import WOrankingSpider
from spiders.cuaaranking import CUAArankingSpider

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import json
import xlwt
import time
import logging

ISOTIMEFORMAT='%Y%m%d%H%M%S'

#xls_filename = "WORanking_" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"
xls_filename = "CUAARanking_" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"

#log_filename = "woranking_" + str(time.strftime(ISOTIMEFORMAT)) + ".log"
log_filename = "cuaaranking_" + str(time.strftime(ISOTIMEFORMAT)) + ".log"

logging.basicConfig(level=logging.INFO, filename=log_filename)
logging.info("=============================================================")
logging.info("logging begin here ...")
logging.info("=============================================================")

#json_file_shanghai = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_shanghairanking_v2.json")
#json_file_qs = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_QS_ARWU_v2.json")
#json_file_webometrics = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_webometrics_v2.json")
json_file_cuaa = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_cuaa_v2.json")
#config_rules_shanghai = json.load(json_file_shanghai)
#config_rules_qs = json.load(json_file_qs)
#config_rules_webometrics = json.load(json_file_webometrics)
config_rules_cuaa = json.load(json_file_cuaa)
#json_file_shanghai.close()
#json_file_qs.close()
#json_file_webometrics.close()
json_file_cuaa.close()

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

logging.info("process: %s " % process)

for ranking_name in config_rules_cuaa:
    print ranking_name
    worksheet = workbook.add_sheet(ranking_name)
    #process.crawl(ShanghairankingSpider, config_rules_shanghai[ranking_name], worksheet)
    #process.crawl(WOrankingSpider, config_rules_webometrics[ranking_name], worksheet, logging)
    process.crawl(CUAArankingSpider, config_rules_cuaa[ranking_name], worksheet,
            logging)

logging.info("process.start() here ...")
process.start() # the script will block here until the crawling is finished


# save workboot
logging.info("before save workbook ...")
#workbook.save("ShanghaiRanking.xls")
workbook.save(xls_filename)
logging.info("after save workbook ...")

