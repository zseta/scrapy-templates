#
# This file was created by Attila Toth - http://scrapingauthority.com
#
#
# This template is usable for TWO-LEVEL DEEP scrapers with pagination on the 1st level.
#
# HOW THE LOOP WORKS:
#
# 1. FOLLOWING LEVEL 1: Follow item urls.
# 2. SCRAPING LEVEL 2: Scrape the fields and populate item.
# 3. PAGINATION LEVEL 1: Go to the next page with the "next button" if any.
# 1. ...
#
#


from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.spiders import Spider
from scrapy import Request
from w3lib.html import remove_tags


class MySpider(Spider):
    name = ''
    start_urls = ['']  # LEVEL 1

    # 1. FOLLOWING LEVEL 1
    def parse(self, response):
        for follow_url in response.css('').extract():
            yield response.follow(follow_url, self.populate_item)
        yield self.paginate(response)

    # 2. SCRAPING LEVEL 2
    def populate_item(self, response):
        item_loader = ItemLoader(item=MySpiderItem(), response=response)
        item_loader.default_input_processor = MapCompose(remove_tags)

        # item_loader.add_css("", "")
        yield item_loader.load_item()

    # 3. PAGINATION LEVEL 1
    def paginate(self, response):
        next_page_url = response.css('').extract_first()  # pagination("next button") <a> element here
        if next_page_url is not None:
            return response.follow(next_page_url, self.parse)

