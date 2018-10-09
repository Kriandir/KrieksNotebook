
import scrapy
import json
import time
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = "viezier"


    def start_requests(self):

        jsonFile = open("tgpos.json","r+")
        datalist = json.load(jsonFile)
        # print len(datalist)
        print datalist
        entry = datalist.pop(0)
        # print entry
        print datalist
        jsonFile.seek(0)  # rewind
        json.dump(datalist, jsonFile)
        jsonFile.truncate()
        # # jsonFile.close()
        # # print len(datalist)
        # # print datalist
        # with open("tgspos.json","w") as outfile:
        #     print datalist
        #     json.dump(datalist,outfile)
        # for entry in datalist:
        yield scrapy.Request(url=entry['url'], callback=self.next,meta={'id':entry['id'],'pos':entry['pos']})

        # jsonFile = open("fluxvar.json",'r')
        # datalist = json.load(jsonFile)







        # for i in self.sourcevarlist:
        #     if i['id'] ==str(15302):
        #         print i

    def next(self,response):
        hsize = "0.5"
        hpos = response.meta['pos']
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'hPOS': hpos, 'hSIZE': hsize},
            callback=self.parse,meta={'id':response.meta['id'],'pos':response.meta['pos']}
        )

    def parse(self, response):
        rows = response.css("table.results tr")[1:]
        data = rows[0].css('td::text').extract()[-2]

        yield {
            'field': data,
            'id':response.meta['id'],
            'pos':response.meta['pos']

        }
