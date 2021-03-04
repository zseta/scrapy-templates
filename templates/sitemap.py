# coding=utf-8
#
# This file was created by Attila Toth - http://scrapingauthority.com
#
#
# This template is usable for websites that have proper sitemaps
#
# sitemap_urls --> url leading to the sitemap xml (or robots.txt that contains sitemap url)
# sitemap_rules --> regex to filter URLs in the sitemap, if passed then proceeds with the given function
#
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import SitemapSpider
from w3lib.html import remove_tags


class MySpider(SitemapSpider):
    name = 'my_spider'
    sitemap_urls = ['https://www.example.com/sitemap.xml']
    sitemap_rules = [
        ('/something/', 'scrape_product'),
    ]

    def scrape_product(self, response):
        item_loader = ItemLoader(item=MyItem(), response=response)
        item_loader.default_input_processor = MapCompose(remove_tags)
        item_loader.default_output_processor = TakeFirst()

        item_loader.add_css('my_field', 'selector')

        return item_loader.load_item()