from spiders.shanghairanking import ShanghairankingSpider
from spiders.qsranking import QSrankingSpider
from spiders.webometricsranking import WOrankingSpider
from spiders.cuaaranking import CUAArankingSpider
from spiders.usnewsranking import USNEWSrankingSpider
from spiders.timesranking import TIMESrankingSpider
from spiders.rankingspider import RankingSpider

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import json
import xlwt
import time
import logging

ISOTIMEFORMAT='%Y%m%d%H%M%S'

log_filename = "rankingspider" + str(time.strftime(ISOTIMEFORMAT)) + ".log"

logging.basicConfig(level=logging.INFO, filename=log_filename)
logging.info("=============================================================")
logging.info("logging begin here ...")
logging.info("=============================================================")

json_file_shanghai = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_shanghairanking_v2.json")
json_file_qs = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_qs_v2.json")
json_file_webometrics = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_webometrics_v2.json")
json_file_cuaa = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_cuaa_v2.json")
#json_file_nseac = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_nseac_v2.json")
json_file_nseac_2015 = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_nseac_2015_v2.json")
json_file_nseac_2016 = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_nseac_2016_v2.json")
json_file_usnews = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_usnews_v2.json")
json_file_times = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_times_v2.json")
json_file_fudanmed = file("/home/joy/Git/GraduationProject_PythonCrawler/webspider/webspider/spiders/config_fudanmed_v2.json")

config_rules_shanghai = json.load(json_file_shanghai)
config_rules_qs = json.load(json_file_qs)
config_rules_webometrics = json.load(json_file_webometrics)
config_rules_cuaa = json.load(json_file_cuaa)
#config_rules_nseac = json.load(json_file_nseac)
config_rules_nseac_2015 = json.load(json_file_nseac_2015)
config_rules_nseac_2016 = json.load(json_file_nseac_2016)
config_rules_usnews = json.load(json_file_usnews)
config_rules_times = json.load(json_file_times)
config_rules_fudanmed = json.load(json_file_fudanmed)

json_file_shanghai.close()
json_file_qs.close()
json_file_webometrics.close()
json_file_cuaa.close()
#json_file_nseac.close()
json_file_nseac_2015.close()
json_file_nseac_2016.close()
json_file_usnews.close()
json_file_times.close()
json_file_fudanmed.close()

config_rules_all = {}
#config_rules_all[ config_rules_times["XLS_FILENAME"] ] = config_rules_times
#config_rules_all[ config_rules_usnews["XLS_FILENAME"] ] = config_rules_usnews
#config_rules_all[ config_rules_cuaa["XLS_FILENAME"] ] = config_rules_cuaa
#config_rules_all[ config_rules_nseac["XLS_FILENAME"] ] = config_rules_nseac
#config_rules_all[ config_rules_nseac_2015["XLS_FILENAME"] ] = config_rules_nseac_2015
config_rules_all[ config_rules_nseac_2016["XLS_FILENAME"] ] = config_rules_nseac_2016
#config_rules_all[ config_rules_webometrics["XLS_FILENAME"] ] = config_rules_webometrics
#config_rules_all[ config_rules_qs["XLS_FILENAME"] ] = config_rules_qs
#config_rules_all[ config_rules_fudanmed["XLS_FILENAME"] ] = config_rules_fudanmed
#config_rules_all[ config_rules_shanghai["XLS_FILENAME"] ] = config_rules_shanghai

# storing workbooks for all website
WorkBooks = {}

settings = Settings()
logging.info("settings: %s" % settings)
logging.info("Settings['DOWNLOAD_DELAY']: %s" % settings['DOWNLOAD_DELAY'])
settings.set('DOWNLOAD_DELAY', 3)
settings.set('RETRY_TIMES', 5)
logging.info("Settings['DOWNLOAD_DELAY']: %s" % settings['DOWNLOAD_DELAY'])
logging.info("Settings['RETRY_TIMES']: %s" % settings['RETRY_TIMES'])
# will set the delay for WO only, in __init__() later ...


process = CrawlerProcess(settings)

logging.info("process: %s " % process)

for website_name in config_rules_all:
    # open Workbook for each website
    WorkBooks[website_name] = xlwt.Workbook(encoding='utf-8', style_compression=0)
    logging.info("WorkBooks: %s" % WorkBooks)
    for ranking_name in config_rules_all[website_name]:
        if ranking_name != "XLS_FILENAME":
            print ranking_name
            worksheet = WorkBooks[website_name].add_sheet(ranking_name)
            process.crawl(RankingSpider, config_rules_all[website_name][ranking_name], worksheet, logging)

logging.info("process.start() here ...")
process.start() # the script will block here until the crawling is finished


# save workboot
logging.info("before save workbook ...")
#workbook.save("ShanghaiRanking.xls")
for workbook in WorkBooks:
    xls_filename = workbook + "ranking-" + str(time.strftime(ISOTIMEFORMAT)) + ".xls"
    WorkBooks[workbook].save(xls_filename)
    logging.info("WorkBooks saving %s" % xls_filename)
logging.info("after save workbook ...")

