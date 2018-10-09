import json


def WriteFluxJson(sources,pos = False,tg = True):
    sourcelist = []
    if not pos:
        try:
            os.remove('fluxvar.json')
        except:
            pass
        name = 'fluxvar'
        for i in sources:
            if i.ra < 0:
                ra = i.ra+360
                ra = "%0.4f" % ra
        	ra = "%0.4f" % i.ra
        	dec = "%0.4f" %i.dec
            data = {'url':"http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=VIII/85A/spectra&-c="+ra+"%2B"+dec+"&-c.u=arcsec&-c.r=5&-out.add=_r&-sort=_r",'id':str(i.id)}
            sourcelist.append(data)
    else:
        if tg:
            try:
                os.remove('tgpos.json')
            except:
                pass
            name = 'tgpos'
            for i in sources:
            	ra = "%0.4f" % i.ra
            	dec = "%0.4f" %i.dec
                pos = ra + " " + dec
                data = {'url':"https://vo.astron.nl/tgssadr/q_fits/cutout/form",'id':str(i.id),'pos':pos}
                sourcelist.append(data)

    with open(name + '.json','w') as outfile:
        json.dump(sourcelist,outfile)
