
import scrapy
import json
import time
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = "viezier"


    def start_requests(self):
        # opens json file and pops first entry
        jsonFile = open("tgpos.json","r+")
        datalist = json.load(jsonFile)
        entry = datalist.pop(0)
        jsonFile.seek(0)  # rewind
        json.dump(datalist, jsonFile)
        jsonFile.truncate()

        # runs the scraper
        yield scrapy.Request(url=entry['url'], callback=self.next,meta={'id':entry['id'],'pos':entry['pos'],'name':entry['name']})


    def next(self,response):
        hsize = "0.25"
        hpos = response.meta['pos']
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'hPOS': hpos, 'hSIZE': hsize},
            callback=self.parse,meta={'id':response.meta['id'],'pos':response.meta['pos'],'name':response.meta['name']}
        )

    def parse(self, response):
        rows = response.css("table.results tr")[1:]
        data = rows[0].css('td::text').extract()[-2]
        positions = response.meta['pos'].split(" ")

        yield {
            'url': "https://vo.astron.nl/getproduct/tgssadr/fits/" + str(data)+".MOSAIC.FITS?sdec=0.25\&dec="+positions[1]+"\&ra="+positions[0]+"\&sra=0.389864794547",
            'id':response.meta['id'],
            'name':response.meta['name']

        }
