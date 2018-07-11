import numpy as np
import pandas as pd
import sys,os

# tiny class wrapper around the tgssdata for ease of access
class datawrapp(object):
    def __init__(self,name,ra,rae,dec,dece,pflux,pfluxe,freq):

        self.radec = np.stack((ra,dec),axis = -1)
        self.ra = ra
	self.name = name
	if name == "tgss":
            self.rae = rae/3600
        else:
            self.rae = rae
        self.dec = dec
        if self.name == "tgss":
            self.dece = dece/3600
        else:
            self.dece = dece
        self.pflux = pflux
        self.pfluxe = pfluxe
        self.freq = freq
        self.keys = ['name','radec','ra','rae','dec','dece','pflux','pfluxe','freq']

# fucntion to call whether to check tgss or vssr
def ReadData(database):
    path = os.getcwd()

    if database == "tgss":
        for y in os.listdir(path):
            if "tgss" in y:
		if "csv" in y:
                    data = pd.read_csv(str(y))
		if "xls" in y:
		    data = pd.read_excel(str(y),sheet_name = "tgss") 
                dataset = datawrapp("tgss",np.array(data.RA),np.array(data.e_RA),\
                np.array(data.DEC),np.array(data.e_DEC),np.array(data.Spk/1000.),\
                np.array(data.e_Spk/1000.),147.5)

    if database == "vlssr":
        for y in os.listdir(path):
            if "vlssr" in y:
		print y
		if "csv" in y:	
                    data = pd.read_csv(str(y))
		if "xls" in y:
                    data = pd.read_excel(str(y),sheet_name = "vlssr")
                dataset = datawrapp("vlssr",np.array(data.ra),[],\
                np.array(data.dec),[],np.array(data.flux_74_mhz/1000.),\
                np.array(data.flux_74_mhz_error/1000.),74)
    return dataset
