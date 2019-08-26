import json


def WriteFluxJson(name,pos,hsize):
    if name == "tgss":
        data = {'url':"https://vo.astron.nl/tgssadr/q/cone/form",'pos':pos,'hsize':hsize,'name':name}

    with open(name + 'data.json','w') as outfile:
        json.dump(data,outfile)

