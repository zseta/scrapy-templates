#
# This file was created by Attila Toth - http://scrapingauthority.com
#
#
# This template is usable for TWO-LEVEL DEEP scrapers with pagination on the 2nd level.
#
#
#
# HOW THE LOOP WORKS:	
#
# 1. FOLLOWING: Follow the 1st available url of an item.
# 2. SCRAPING: Scrape the fields and populate item.
# 3. PAGINATION: Go to the next page with the "next button" if any.
# 2. ...
# 3. ...
#


from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.spiders import Spider
from scrapy import Request
from w3lib.html import remove_tags


class MySpider(Spider):
    name = ''
    start_urls = ['']  # FIRST LEVEL

    # 1. FOLLOWING
    def parse(self, response):
        # url(href attribute) which leads to the(SECOND LEVEL) page where data extraction is needed
        follow = response.css('').extract_first()
        follow_url = response.urljoin(follow)
        # request the url and callback the function that extracts data
        yield Request(follow_url, callback=self.populate_item)

    # 2. SCRAPING LEVEL 2
    def populate_item(self, response):
        item_loader = ItemLoader(item=MySpiderItem(), response=response)
        item_loader.default_input_processor = MapCompose(remove_tags)

        # item_loader.add_css("")
        # item_loader.add_value("raw", raw)

        # yield the populated item first
        yield item_loader.load_item()
        # then yield the function which paginates to another page that contains data
        yield self.paginate(response)

    # 3. PAGINATION LEVEL 2
    def paginate(self, response):
        next_page_url = response.css('').extract_first()  # pagination("next button") <a> element here
        if next_page_url is not None:
            return response.follow(next_page_url, self.populate_item)

