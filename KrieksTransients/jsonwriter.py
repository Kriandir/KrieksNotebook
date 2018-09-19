# import json

# data = {'url':"http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=VIII/85A/spectra&-c=185.7163%2B50.4487&-c.u=arcsec&-c.r=5&-out.add=_r&-sort=_r",'id':2312}
#
# data.update({'url':"http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=VIII/85A/spectra&-c=182.7163%2B50.4487&-c.u=arcsec&-c.r=5&-out.add=_r&-sort=_r",'id':1243})
# # print data
# # with open('data.json', 'w') as outfile:
#

import json


def WriteFluxJson(sources):
    sourcelist = []
    for i in sources:
        data = {'url':"http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=VIII/85A/spectra&-c="+"%0.4f"+"%2B"+"%0.4f"+"&-c.u=arcsec&-c.r=5&-out.add=_r&-sort=_r" %(i.ra,i.dec),'id':i.id}
        sourcelist.append(data)
    print sources.ra
    print sources.dec
    print sourcelist
# multikeys = []
# data = {'url':"http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=VIII/85A/spectra&-c=185.7163%2B50.4487&-c.u=arcsec&-c.r=5&-out.add=_r&-sort=_r",'id':2312}
# multikeys.append(data)
# data = {'url':"http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=VIII/85A/spectra&-c=182.7163%2B50.4487&-c.u=arcsec&-c.r=5&-out.add=_r&-sort=_r",'id':1243}
# multikeys.append(data)
# # for i in range(3):
# #     multikeys.append(data)
# print multikeys
# with open('data.json', 'w') as outfile:
#     json.dump(multikeys,outfile)
