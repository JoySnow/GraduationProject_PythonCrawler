# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider

import xlwt


#class ShanghairankingItem(scrapy.Item):
#        world_ranking = scrapy.Field()
#        schoolname = scrapy.Field()
#        location = scrapy.Field()
#        nation_ranking = scrapy.Field()
#        total_score = scrapy.Field()
#        index_alumni = scrapy.Field()
#        index_award = scrapy.Field()
#        index_hici = scrapy.Field()
#        index_ns = scrapy.Field()
#        index_pub = scrapy.Field()
#        index_pcp = scrapy.Field()
#        index_top = scrapy.Field()


class ShanghairankingSpider(CrawlSpider):
    name = "Shanghairanking"

    def __init__(self, rule, worksheet):
       self.rule = rule
       self.name = self.rule["ranking_name"]
       print "=============================="
       print "self.rule[start_urls]: ", self.rule["start_urls"]
       print "type(): ", type(self.rule["start_urls"])
       self.start_urls = [self.rule["start_urls"],]

       self.worksheet = worksheet

    def parse(self, response):
        row_index = 0
        for select in response.xpath(self.rule["table_tag"]):
            #print "select: ", select
            #print "self.rule[\"columns\"]: ", self.rule["columns"]
            if row_index == 0:
                for col in self.rule["columns"]:
                    data = select.xpath(self.rule["columns"][col]["title"]).extract()
                    #print "data: ", data
                    self.worksheet.write(row_index, int(col)-1, data)
            else:
                for col in self.rule["columns"]:
                    data = select.xpath(self.rule["columns"][col]["content"]).extract()
                    #print "data: ", data
                    self.worksheet.write(row_index, int(col)-1, data)
            row_index += 1


