# -*- coding: utf-8 -*-
import scrapy

#import json
import xlwt



#json_file = file("./config_shanghairanking.json")
#config_rules = json.load(json_file)

book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('ranking', cell_overwrite_ok=True)

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


class ShanghairankingSpider(scrapy.Spider):

    def __init__(self, rule):
       self.rule = rule
       self.name = rule["ranking_name"]
       self.start_urls = rule["start_urls"]

    def parse(self, response):
        row_index = 1
        for select in response.xpath(self.rule["table_tag"]):
            if row_index == 1:
                for col in self.rule["columns"]:
                    data = select.xpath(self.rule["columns"]["col"]["world_ranking_t"])
                    sheet.write(row_index, col, data)
            else:
                for col in self.rule["columns"]:
                    data = select.xpath(self.rule["columns"]["col"]["world_ranking_c"])
                    sheet.write(row_index, col, data)
            row_index += 1




#    def parse(self, response):
#        book = xlwt.Workbook(encoding='utf-8',style_compression=0)
#        sheet = book.add_sheet('ranking', cell_overwrite_ok=True)
#        row = col = 0
#        for sel in response.xpath('//table/tbody/tr'): //each row in table
#            if (row == 0):                          //first row for title
#                for index in sel.xpath('th'):     //each column in table
#                    #item.appand(col.xpath('text()').extract())
#                    if index.xpath('form'):
#                        data = index.xpath('form//option[@value]').extract()
#                    else:
#                        data = index.xpath('text()').extract()
#                    sheet.write(row, col, data)
#                    col += 1
#            else:                                   //the content row
#                #for index in sel.xpath('td')
#                #sheet.write(row, )
#                TBD:
#                    dont know how to put it, if using loop, then lots of 'if' will
#                    come, and its so detailed selections.
#                    So, How to put it ??????
#
#            row += 1
#            col = 0
#        //end of the mai for loop
