# -*- coding: utf-8 -*-
import scrapy

#Scraping an official site for scraping
class Quotes(scrapy.Spider):
    allowed_domain='http://quotes.toscrape.com/'
    name='qpra'
    start_urls=["http://quotes.toscrape.com/"]
    
    def parse(self,response):
            quote=response.xpath("//*[@class='quote']")
            for q in quote:
                quotes=q.xpath(".//*[@class='text']/text()").extract_first()
                author=q.xpath(".//*[@class='author']/text()").extract_first()
                tags=q.xpath(".//*[@itemprop='keywords']/@content").extract_first()
                yield{'Quotes':quotes,
                    'Author':author,
                    'Tags':tags}
            next_page_url=response.xpath("//*[@class='next']/a/@href").extract_first()
            absolute_next_page_url=response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)
            

        

        