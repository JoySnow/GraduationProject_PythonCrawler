from spiders.shanghairanking import ShanghairankingSpider
from spiders.qsranking import QSrankingSpider
from spiders.webometricsranking import WOrankingSpider
from spiders.cuaaranking import CUAArankingSpider
from spiders.usnewsranking import USNEWSrankingSpider
from spiders.timesranking import TIMESrankingSpider

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import json
import xlwt
import time
import logging

ISOTIMEFORMAT='%Y%m%d%H%M%S'

xls_filename = "QSRanking_" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"
#xls_filename = "WORanking_" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"
#xls_filename = "CUAARanking_" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"
#xls_filename = "NSEACRanking_" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"
#xls_filename = "USNEWSRanking_" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"
#xls_filename = "TIMESRanking_" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"

log_filename = "qsranking_" + str(time.strftime(ISOTIMEFORMAT)) + ".log"
#log_filename = "woranking_" + str(time.strftime(ISOTIMEFORMAT)) + ".log"
#log_filename = "cuaacranking_" + str(time.strftime(ISOTIMEFORMAT)) + ".log"
#log_filename = "nseacranking_" + str(time.strftime(ISOTIMEFORMAT)) + ".log"
#log_filename = "usnewsranking_" + str(time.strftime(ISOTIMEFORMAT)) + ".log"
#log_filename = "timesranking_" + str(time.strftime(ISOTIMEFORMAT)) + ".log"

logging.basicConfig(level=logging.INFO, filename=log_filename)
logging.info("=============================================================")
logging.info("logging begin here ...")
logging.info("=============================================================")

#json_file_shanghai = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_shanghairanking_v2.json")
json_file_qs = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_qs_v2.json")
#json_file_webometrics = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_webometrics_v2.json")
#json_file_cuaa = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_cuaa_v2.json")
#json_file_nseac = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_nseac_v2.json")
#json_file_usnews = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_usnews_v2.json")
#json_file_times = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_times_v2.json")

#config_rules_shanghai = json.load(json_file_shanghai)
config_rules_qs = json.load(json_file_qs)
#config_rules_webometrics = json.load(json_file_webometrics)
#config_rules_cuaa = json.load(json_file_cuaa)
#config_rules_nseac = json.load(json_file_nseac)
#config_rules_usnews = json.load(json_file_usnews)
#config_rules_times = json.load(json_file_times)

#json_file_shanghai.close()
json_file_qs.close()
#json_file_webometrics.close()
#json_file_cuaa.close()
#json_file_nseac.close()
#json_file_usnews.close()
#json_file_times.close()

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

for ranking_name in config_rules_qs:
    print ranking_name
    worksheet = workbook.add_sheet(ranking_name)
    #process.crawl(ShanghairankingSpider, config_rules_shanghai[ranking_name], worksheet)
    process.crawl(QSrankingSpider, config_rules_qs[ranking_name], worksheet, logging)
    #process.crawl(WOrankingSpider, config_rules_webometrics[ranking_name], worksheet, logging)

    # cuaa & nseac should share the same spider named CUAArankingSpider
    #process.crawl(CUAArankingSpider, config_rules_cuaa[ranking_name], worksheet, logging)
    #process.crawl(CUAArankingSpider, config_rules_nseac[ranking_name], worksheet, logging)

    #process.crawl(USNEWSrankingSpider, config_rules_usnews[ranking_name], worksheet, logging)
    #process.crawl(TIMESrankingSpider, config_rules_times[ranking_name], worksheet, logging)

logging.info("process.start() here ...")
process.start() # the script will block here until the crawling is finished


# save workboot
logging.info("before save workbook ...")
#workbook.save("ShanghaiRanking.xls")
workbook.save(xls_filename)
logging.info("after save workbook ...")

