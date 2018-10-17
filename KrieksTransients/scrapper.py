
import scrapy
import json
import time
from scrapy.crawler import CrawlerProcess
class QuotesSpider(scrapy.Spider):
    name = "viezier"

    def start_requests(self):

        jsonFile = open("fluxvar.json",'r')
        datalist = json.load(jsonFile)


        for entry in datalist:

            yield scrapy.Request(url=entry['url'], callback=self.next,\
            meta={'id':entry['id']})
        # for i in self.sourcevarlist:
        #     if i['id'] ==str(15302):
        #         print i

    def next(self,response):
        yield scrapy.http.FormRequest.from_response(response,callback=self.parse,\
        meta={'id':response.meta['id']})

    def parse(self, response):

        rows = response.css("table.sort tr")[1:]
        # nu = []
        # s_nu = []
        # e = []
        if rows:
            for row in rows:
                data = row.css('td::text').extract()[4:7]
                # nu.append(data[0])
                # s_nu.append(data[1])
                # e.append(data[2])
                nu = data[0]
                s_nu = data[1]
                e = data[2]

            # sourcedict = {
            #     'nu':nu,
            #     's_nu':s_nu,
            #     'e':e,
            #     'id':response.meta['id']
            #
            #
            # }
            # with open('dict.csv', 'w') as f:
            #     [f.write('{0},{1}\n'.format(key, value)) for key, value in sourcedict.items()]
            # if response.meta['id'] == str(10500):
            #     print '-##########-'
            #     print sourcedict
            #     print '--#########--'

                yield {
                    'nu': nu,
                    's_nu': s_nu,
                    'e': e,
                    'id':response.meta['id']
                }
        else:
            yield {
                'nu': [],
                's_nu': [],
                'e': [],
                'id':response.meta['id']
            }
        # sourcedict ={
        # 'id':self.ids,
        # 'nu':nu,
        # 's_nu':s_nu,
        # 'e':e
        # }
        # self.sourcevarlist.append(sourcedict)
        # print sourcedict
        # globalfinalsourcelist

# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# })
#
# d = process.crawl(QuotesSpider)
# process.start()
