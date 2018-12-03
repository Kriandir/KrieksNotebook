import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.nddata.utils import Cutout2D
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS


imagefile = "../IMAGES/December/26_8192_4asec_all_1hr/1hr_allband_autothresh-t0004-image-pb.fits"

def PlotterFunction(image_data,c,wcss,ids,size,database = 'own'):

    # GET CUTOUT AND PLOT IT
    plt.figure(figsize = (10,10))
    cutout1 = Cutout2D(image_data, c,size,wcs=wcss)
    plt.imshow(cutout1.data, origin='lower')
    plt.colorbar()
    plt.savefig(str(ids)+"cutout_"+database+".png")
    plt.show()

def GetCutout(imagefile,ra,dec,ids,pixels,database = 'own'):
    hdu_list = fits.open(imagefile)

    image_data = hdu_list[0].data
    w= WCS(hdu_list[0].header)


    # GET LOCATION OF SOURCE
    size = u.Quantity(pixels, u.pixel)
    c = SkyCoord(ra, dec, frame='fk5', unit='deg')


    # DEFINE WCS COORDINATE SYSTEM
    wcss = WCS(naxis=2)
    wcss.wcs.ctype = ['RA---SIN','DEC--SIN']
    wcss.wcs.crval = [w.wcs.crval[0],w.wcs.crval[1]]
    wcss.wcs.crpix = [ w.wcs.crpix[0],w.wcs.crpix[1]]
    try:
        wcss.wcs.cdelt = [w.wcs.cdelt[0],w.wcs.cdelt[1]]
        # RESHAPE DATA IN PROPER IMAGE FORMAT
        shape = (image_data.shape)
        image_data = image_data.reshape((shape[2],shape[3]))
        if database:
            PlotterFunction(image_data,c,wcss,size,ids,database)
        else:
            PlotterFunction(image_data,c,wcss,size,ids)
        # if database == 'vlsrr':
            # size = u.Quantity((60,60),u.pixel)
    except:
        try:
            shape = (image_data.shape)
            image_data = image_data.reshape((shape[2],shape[3]))
            wcss.wcs.cd = [w.wcs.cd[0],w.wcs.cd[1]]
            if database:
                PlotterFunction(image_data,c,wcss,size,ids,database)
            else:
                PlotterFunction(image_data,c,wcss,size,ids)
        except:
            print "something went fatally wrong check the script"
    hdu_list.close()
