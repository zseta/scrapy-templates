#
# This file was created by Attila Toth - http://scrapingauthority.com
#
#
# This template is usable for ONE-LEVEL DEEP scrapers with pagination.
#
# HOW THE LOOP WORKS:
#
# 1. SCRAPING LEVEL 1: Scrape fields and populate item.
# 2. PAGINATION LEVEL 1: Go to the next page with the "next button" if any.
# 1. ...
#
#

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import Spider
from scrapy import Request
from w3lib.html import remove_tags

class MySpider(Spider):
    name = ''
    start_urls = [''] #FIRST LEVEL

    def parse(self, response):
        for item_box in response.css(''):  # define a "box" which contains the fields for ONE SINGLE item
            yield self.populate_item(item_box)

        # 2. PAGINATION
        next_page_url = response.css('').extract_first()  # pagination("next button") <a> element here
        if next_page_url is not None:
            yield response.follow(next_page_url, self.populate_item)

    # 1. SCRAPING
    def populate_item(self, selector):
        item_loader = ItemLoader(item=MySpiderItem(), selector=selector)
        item_loader.default_input_processor = MapCompose(remove_tags)
        item_loader.default_output_processor = TakeFirst()
        #
        #item_loader.add_css("my_field", "my_css")
        #item_loader.add_xpath("my_field", "my_xpath")
        #
        return item_loader.load_item()
