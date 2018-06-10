import numpy as np
import pandas as pd

# tiny class wrapper around the tgssdata for ease of access
class datawrapp(object):
    def __init__(self,name,ra,rae,dec,dece,pflux,pfluxe,freq,iflux,ifluxe):

        self.radec = np.stack((ra,dec),axis = -1)
        self.ra = ra
	if name == "tgss":
            self.rae = rae/3600
        else:
            self.rae = rae
        self.dec = dec
        if name == "tgss":
            self.dece = dece/3600
        else:
            self.dece = dece
        self.pflux = pflux
        self.pfluxe = pfluxe
        self.freq = freq
        self.iflux = iflux
        self.ifluxe = ifluxe
        self.keys = ['radec','ra','rae','dec','dece','pflux','pfluxe','freq']
        if not iflux:
            continue
        else:
            self.keys.append('iflux')
            self.keys.append('ifluxe')

# fucntion to call whether to check tgss or vssr
def ReadData(database):

    if database == "tgss":
        data = pd.read_csv("tgsscutout.csv")
        dataset = datawrapp("tgss",np.array(data.RA),np.array(data.e_RA),\
        np.array(data.DEC),np.array(data.e_DEC),np.array(data.Spk/1000),\
        np.array(data.e_Spk/1000),147.5,np.array(data.Sint/1000),\
        np.array(data.e_Sint/1000))

    if database == "vssr":
        data = pd.read_excel("vssrdataset.xls",sheet_name = "vlssr")
        dataset = datawrapp("vssr",np.array(data.ra),[],\
        np.array(data.dec),[],np.array(data.flux_74_mhz),\
        np.array(data.flux_74_mhz_error),74,[],[])
    return dataset
