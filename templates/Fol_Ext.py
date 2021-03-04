#
# This file was created by Attila Toth - http://scrapingauthority.com
#
#
# This template is usable for TWO-LEVEL DEEP scrapers.
#
#
# HOW IT WORKS:
#
# 1. FOLLOWING: Follow the urls specified in rules.
# 2. SCRAPING: Scrape the fields and populate item.
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

    # 1. FOLLOWING LEVEL 1
    rules = (
        Rule(LinkExtractor(restrict_css=''), callback='populate_item'),
    )

    # 2. SCRAPING level 2
    def populate_item(self, response):
        item_loader = ItemLoader(item=MySpiderItem(), response=response)
        item_loader.default_input_processor = MapCompose(remove_tags)

        #item_loader.add_css("", "")
        #item_loader.add_css("", "")

        yield item_loader.load_item()
