
import scrapy
from scrapy.crawler import CrawlerProcess
class QuotesSpider(scrapy.Spider):
    name = "viezier"

    def start_requests(self):
        print 'hoi'
        with open('urls.txt', 'rb') as urls:
        # start_urls = [
        #     'http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=VIII/85A/spectra&-c=185.7163%2B50.4487&-c.u=arcsec&-c.r=5&-out.add=_r&-sort=_r'
        # ]

            for url in urls:
                yield scrapy.Request(url=url, callback=self.next)

    def next(self,response):
        yield scrapy.http.FormRequest.from_response(response,callback=self.parse)

    def parse(self, response):
        rows = response.css("table.sort tr")[1:]
        for row in rows:
            data = row.css('td::text').extract()[4:7]
            nu = data[0]
            s_nu = data[1]
            e = data[2]
            yield {
                'nu': nu,
                's_nu': s_nu,
                'e': e,
            }
# process = CrawlerProcess({
    # 'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# })

# d = process.crawl(QuotesSpider)
# process.start()
