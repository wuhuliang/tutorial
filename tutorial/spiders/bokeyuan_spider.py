# -*- coding: utf-8 -*-
import scrapy
from  tutorial.items import TutorialItem


class BokeyuanSpiderSpider(scrapy.Spider):
    name = 'bokeyuan_spider'
    allowed_domains = ['cnblog.com']
    start_urls = ('https://www.cnblogs.com/news/',
                  'https://www.cnblogs.com/pick/')

    def parse(self, response):
        # filename = response.url.split('/')[3] + ".html"
        # with open(filename,'wb') as fp:
        #     fp.write(response.body)
        divs = response.xpath('//*[@id="post_list"]/div/div[2]/p')
        for x in divs:
            item = TutorialItem()
            item['desc'] = x.xpath('text()').extract()
            yield item
