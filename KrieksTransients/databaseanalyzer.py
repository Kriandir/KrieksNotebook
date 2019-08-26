
import scrapy
import json
import time
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = "viezier"


    def start_requests(self):
        # opens json file and pops first entry
        jsonFile = open("tgssdata.json","r+")
        datalist = json.load(jsonFile)
        print '\n\n\n\n\n\n\n\n\n----------------'
        print datalist
        entry = datalist
        print entry['url']

        # runs the scraper
        yield scrapy.Request(url=entry['url'], callback=self.next,meta={'pos':entry['pos'],'hsize':entry['hsize'],'name':entry['name']})


    def next(self,response):
        hsize = response.meta['hsize']
        hpos = response.meta['pos']
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'hscs_pos': hpos, 'hscs_sr': hsize},
            callback=self.parse,meta={'pos':response.meta['pos'],'hsize':response.meta['hsize'],'name':response.meta['name']}
        )

    def parse(self, response):


        rows = response.css("table tr")[1:]
        if rows:
            for row in rows:
                data = row.css('td::text').extract()
                dist = data[0]
                id = data[1]
                ra = data[2]
                rae = data[3]
                dec = data[4]
                dece = data[5]
                sint = data[6]
                sinte = data[7]
                spk = data[8]
                spke = data[9]
                majax = data[10]
                majaxe = data[11]
                minax = data[12]
                minaxe = data[13]
                pa = data[14]
                pae = data[15]
                island_rms = data[16]
                s_code = data[17]
                mosaic_name = data[18]

                yield {
                    'dist': dist,
                    'id': id,
                    'ra': ra,
                    'rae':rae,
                    'dec': dec,
                    'dece': dece,
                    'sint': sint,
                    'sinte':sinte,
                    'spk': spk,
                    'spke': spke,
                    'majax': majax,
                    'majaxe':majaxe,
                    'minax': minax,
                    'minaxe':minaxe,
                    'pa': pa,
                    'pae': pae,
                    'island_rms': island_rms,
                    's_code':s_code,
                    'mosaic_name':mosaic_name
                }
        else:
            yield {
                'nu': [],
                's_nu': [],
                'e': [],
                'id':response.meta['id']
            }
