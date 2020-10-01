import scrapy


class CovSpider(scrapy.Spider):
    name = 'cov'
    allowed_domains = ['covidindia.org']
    start_urls = ['https://covidindia.org/']

    def start_requests(self):
        urls=[
            'https://covidindia.org/',
            ]
        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//*[@class="tablepress tablepress-id-96 tablepress-responsive"]//tbody//tr'):
            yield{
                'state' : row.xpath('td[1]//text()').extract_first(),
                'Confirmed Cases' : row.xpath('td[2]//text()').extract_first(),
                'Recoveries' : row.xpath('td[3]//text()').extract_first(),
                'Deaths' : row.xpath('td[4]//text()').extract_first(),
            }
           
        pass
