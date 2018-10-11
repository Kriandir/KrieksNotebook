import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.nddata.utils import Cutout2D
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS


imagefile = "../IMAGES/December/26_8192_4asec_all_1hr/1hr_allband_autothresh-t0004-image-pb.fits"

def GetCutout(imagefile,ra,dec,id):
    hdu_list = fits.open(imagefile)

    image_data = hdu_list[0].data

    # GET LOCATION OF SOURCE
    size = u.Quantity((120, 120), u.pixel)
    c = SkyCoord(ra, dec, frame='fk5', unit='deg')


    # DEFINE WCS COORDINATE SYSTEM
    wcs = WCS(naxis=2)
    wcs.wcs.ctype = ['RA---SIN','DEC--SIN']

    wcs.wcs.crval = [-174.71428,47.49272]
    wcs.wcs.crpix = [ 4097.0,4097.0]
    wcs.wcs.cdelt = [-0.00111111111111111,0.00111111111111111]

    hdu_list.close()

    # RESHAPE DATA IN PROPER IMAGE FORMAT
    shape = (image_data.shape)
    image_data = image_data.reshape((shape[2],shape[3]))



    # GET CUTOUT AND PLOT IT
    plt.figure(figsize = (10,10))
    cutout1 = Cutout2D(image_data, c,size,wcs=wcs)
    plt.imshow(cutout1.data, origin='lower')
    plt.colorbar()
    plt.savefig(str(id)+"cutout"+".png")
    plt.show()
