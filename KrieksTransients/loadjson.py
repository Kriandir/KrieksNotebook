import json
jsonFile = open("data.json", "r")
data = json.load(jsonFile)
print data[1]['id']
