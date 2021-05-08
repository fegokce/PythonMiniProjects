import scrapy

class ZyteSpider(scrapy.Spider):
    page = input("Page No (1-20): ")
    name = 'zyte'
    allowed_domains = ['www.zyte.com']
    start_urls = [f'https://www.zyte.com/blog/page/{page}/']

    def parse(self, response):
        for blog in response.xpath('//div[@class="oxy-post"]'):
            yield{
                "title" : blog.xpath('.//a[@class="oxy-post-title"]//text()').get(),
                "author" : blog.xpath('.//div[@class="oxy-post-meta-author oxy-post-meta-item"]//text()').get().strip("\n\t\t\t"),
                "link" : blog.xpath('.//a[@class="oxy-read-more"]/@href').get(),
                "date" : blog.xpath('.//div[@class="oxy-post-image-date-overlay"]//text()').get().strip("\n\t\t\t").strip()
            }