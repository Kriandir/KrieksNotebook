import numpy as np
import os,sys
import wget
import json

# Downloads fits files from scraped sites.
datalist = []
s = open('poslink.json', 'r')
for line in s.readlines():
    try:
        j = line.split('|')[-1]
        datalist.append(json.loads(j))
    except ValueError:
        continue

for i in datalist:
    print i
    os.system("wget -O "+ i['id']+i['name']+".fits "+i['url'])
