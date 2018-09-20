import json
import pandas as pd

def Loadin():
    jsonFile = open("neat.json", "r")
    data = json.load(jsonFile)
    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':
    x = Loadin()
    print x['id']
