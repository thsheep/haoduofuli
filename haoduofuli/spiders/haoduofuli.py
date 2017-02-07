from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from haoduofuli.items import HaoduofuliItem


class myspider(CrawlSpider):

    name = 'haoduofuli'
    allowed_domains = ['haoduofuli.pw']
    start_urls = ['http://www.haoduofuli.pw']

    rules = (
        Rule(LinkExtractor(allow=('\.html',)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = HaoduofuliItem()
        try:
            item['url'] = response.url
            item['category'] = response.xpath('//*[@id="content"]/div[1]/div[1]/span[2]/a/text()').extract()[0]
            item['title'] = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract()[0]
            item['imgurl'] = response.xpath('//*[@id="post_content"]/p/img/@src').extract()
            item['yunlink'] = response.xpath('//*[@id="post_content"]/blockquote/a/@href').extract()[0]
            item['password'] = response.xpath('//*[@id="post_content"]/blockquote/font/text()').extract()[0]
            return item
        except:
            item['url'] = response.url
            item['category'] = response.xpath('//*[@id="content"]/div[1]/div[1]/span[2]/a/text()').extract()[0]
            item['title'] = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract()[0]
            item['imgurl'] = response.xpath('//*[@id="post_content"]/p/img/@src').extract()
            item['yunlink'] = response.xpath('//*[@id="post_content"]/blockquote/p/a/@href').extract()[0]
            item['password'] = response.xpath('//*[@id="post_content"]/blockquote/p/span/text()').extract()[0]
            return item





