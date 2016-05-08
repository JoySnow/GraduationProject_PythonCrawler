# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
import time

import xlwt
import logging



class TIMESrankingSpider(CrawlSpider):
    name = "timesranking"

    def __init__(self, rule, worksheet, logging):
        CrawlSpider.__init__(self)
        # use any browser you wish
        self.browser = webdriver.Firefox()
        self.logging = logging
        self.rule = rule
        self.name = self.rule["ranking_name"]
        self.logging.info("==============================")
        self.logging.info("self.rule[start_urls]: %s" % self.rule["start_urls"])
        self.start_urls = self.rule["start_urls"]
        #self.next_page_p = self.rule["next_page_p"]
        self.next_page_click = self.rule["next_page_click"]
        #self.total_pages = int(self.rule["total_pages"]) \
        #                    if self.rule["total_pages"] else 1000000
        #self.logging.info("self.total_pages: %s" % self.total_pages)
        #self.logging.info("type of self.total_pages: %s" % type(self.total_pages))
        self.worksheet = worksheet
        self.logging.info("Finish the __init__ method ... ")

    def __del__(self):
        self.logging.info("=============================================================")
        self.logging.info("logging end here ...")
        self.logging.info("=============================================================")
        self.browser.quit()

    def parse(self, response):

        # these two vals are for callback args
        #   that we passed in Request(next_page_url)
        write_title = ( response.meta['write_title'] \
                        if ('write_title' in response.meta) else True )
        start_row = ( response.meta['start_row'] \
                        if ('start_row' in response.meta) else 0 )
        crawld_pages = ( response.meta['crawld_pages'] \
                        if ('crawld_pages' in response.meta) else 0 )
        logging.info("write_title: %s" % write_title)
        logging.info("start_row %s" % start_row)
        logging.info("crawld_pages %s" % crawld_pages)

        # using browser to get url again ...
        logging.info("****SPECIAL INFO: the url which browser get is %s" % response.url)
        # NOW, change the response.url to self.start_urls[0]
        #self.browser.get(response.url)
        self.browser.get(self.start_urls[0])
        self.logging.info("#### got url ...")
        self.logging.info("#### response: %s" % response)

        # add this to click ALL then all rows in one page
        self.browser.find_element_by_xpath(self.next_page_click).click()

        browser_response = Selector(text = self.browser.page_source)
        #browser_response = response
        logging.info("type(browser_response): %s" % type(browser_response))

        # broswer is ready now ...
        self.logging.info("begin the logic of parse method ... ")


        # crawl data of this page
        # start here
        logging.info("start crawling data of this page ...")

        row_index = start_row

        # for the title of the table
        if write_title:
            for col in self.rule["columns"]:
                if self.rule["columns"][col]["title"] != "None":
                    data = browser_response.xpath(self.rule["columns"][col]["title"]).extract()
                    #print "data: ", data
                    self.worksheet.write(row_index, int(col)-1, data)
            row_index += 1

        # for the content of the table
        for select in browser_response.xpath(self.rule["table_tag"]):
            #logging.info("select: %s" % select)
            #logging.info("self.rule[\"columns\"]: %s" % self.rule["columns"])

            for col in self.rule["columns"]:
                data = select.xpath(self.rule["columns"][col]["content"]).extract()
                #logging.info("data: %s" % data)
                self.worksheet.write(row_index, int(col)-1, data)
            row_index += 1

        crawld_pages += 1
        logging.info("finished crawling data of this page ...")

#        # next_page need to be crawl ...
#        # then do it
#        #  AND this next_page is for usnews, url patten
#        #  self.next_page_p =["url_pattern", "start_page", "end_page"]
#        if self.next_page_p and ( crawld_pages < int(self.next_page_p[2]) ):
#            # 字符串拼凑，替换NUM处的值
#
#        #if len(self.next_pages) > crawld_pages-1:
#            #href = response.xpath(self.next_page)
#            #logging.info("##### href: %s" % href)
#            #logging.info("##### type(href): %s" % type(href))
#            #if href:
#            next_url = self.next_page_p[0].replace("NUM",  str(crawld_pages) )
#            #next_url = self.next_pages[crawld_pages-1]
#            request = scrapy.Request(next_url, callback=self.parse)
#            request.meta['write_title'] = False
#            request.meta['start_row'] = row_index
#            request.meta['crawld_pages'] = crawld_pages
#            return request
#        else:
#            logging.info("No more next_page to crawl ...")
#            logging.info("I will quit my parse here ... Thanks ...")

#        # next_page need to be crawl ...
#        # then do it
#        if len(self.next_pages) > crawld_pages-1:
#            #href = response.xpath(self.next_page)
#            #logging.info("##### href: %s" % href)
#            #logging.info("##### type(href): %s" % type(href))
#            #if href:
#            next_url = self.next_pages[crawld_pages-1]
#            request = scrapy.Request(next_url, callback=self.parse)
#            request.meta['write_title'] = False
#            request.meta['start_row'] = row_index
#            request.meta['crawld_pages'] = crawld_pages
#            return request
#        else:
#            logging.info("No more next_page to crawl ...")
#            logging.info("I will quit my parse here ... Thanks ...")
#
        self.logging.info("Finish the logic of parse method ... ")

