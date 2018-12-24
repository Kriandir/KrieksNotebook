# Script for reading in json file and outputting as pandas
# (for more info email kriekvdmeulen@gmail.com)

import json
import pandas as pd

def Loadin():
    jsonFile = open("neat.json", "r")
    data = json.load(jsonFile)
    df = pd.DataFrame(data)
    return df

#Check function please ignore
if __name__ == '__main__':
    x = Loadin()
    print x['id']
