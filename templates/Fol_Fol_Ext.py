#
# This file was created by Attila Toth - http://scrapingauthority.com
#
#
# This template is usable for TWO-LEVEL DEEP scrapers.
#
#
# HOW IT WORKS:
#
# 1. FOLLOWING: Follow the urls specified in the 1st Rule.
# 2. FOLLOWING: Follow the urls specified in the 2st Rule.
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
        Rule(LinkExtractor(restrict_css=''), follow=True), # LEVEL 1
        Rule(LinkExtractor(restrict_css=''), callback='populate_item'), # LEVEL 2
    )

    # 2. SCRAPING LEVEL 3
    def populate_item(self, response):
        item_loader = ItemLoader(item=MySpiderItem(), response=response)
        item_loader.default_input_processor = MapCompose(remove_tags)

        #item_loader.add_css("", "")
        #item_loader.add_css("", "")

        yield item_loader.load_item()