import json
jsonFile = open("neat.json", "r")
data = json.load(jsonFile)
for i in data:
    if i['id'] == str(15302):
        print i
