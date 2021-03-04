# coding=utf-8
#
# This file was created by Attila Toth - http://scrapingauthority.com
#
#
# This template is usable for THREE-LEVEL DEEP scrapers.
#
#
# HOW IT WORKS:
#
# 1. FOLLOWING: Follow the urls specified in the 1st Rule.
# 2. FOLLOWING: Follow the urls specified in the follow function and paginate on the same level
# 3. SCRAPING: Scrape the fields and populate item.
#
#


from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags

class MySpider(CrawlSpider):
    name = ''
    start_urls = ['']  # LEVEL 1

    # 1. FOLLOWING
    rules = (
        Rule(LinkExtractor(restrict_css=''), callback='follow'), # LEVEL 1
    )

    # 2. FOLLOWING LEVEL 2
    def follow(self, response):
        for follow_url in response.css("").extract():
            yield response.follow(follow_url, self.populate_item)
        yield self.paginate(response)

    # 2. SCRAPING LEVEL 3
    def populate_item(self, response):
        item_loader = ItemLoader(item=MySpiderItem(), response=response)
        item_loader.default_input_processor = MapCompose(remove_tags)

        #item_loader.add_css("field", "")
        yield item_loader.load_item()

    # 3. PAGINATION LEVEL 2
    def paginate(self, response):
        next_page_url = response.css("").extract_first()  # pagination("next button") <a> element here
        if next_page_url is not None:
            return response.follow(next_page_url, self.parse)
