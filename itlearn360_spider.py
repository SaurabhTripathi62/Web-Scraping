# -*- coding: utf-8 -*-
import scrapy
#very straight forward code 

class Itlearn360SpiderSpider(scrapy.Spider):
    name = 'itlearn360_spider'
    allowed_domains = ['itlearn360.com/']
    start_urls = ['http://itlearn360.com//']

    def parse(self, response):
        main_heading=response.xpath('//h4/text()').extract() #main course headings
        all_course= response.xpath('//*[@itemprop="name"]/text()').extract()#all course list
        
        
        for c in all_course:
            
            yield {'Course':c}
        