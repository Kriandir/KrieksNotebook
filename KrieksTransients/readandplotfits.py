import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

# READ IN FITS
def Imager(imagefile):
    hdu_list = fits.open(imagefile)
    hdu_list.info()
    image_data = hdu_list[0].data

    # RESHAPE DATA FOR PROPER FORMAT
    shape = (image_data.shape)
    image_data = np.reshape(image_data,(shape[2],shape[3]))
    hdu_list.close()

    # plot and save the data
    plt.figure(figsize=(10,10))
    plt.imshow(image_data, origin='lower')
    plt.colorbar()
    plt.savefig(imagefile.replace(".fits",".png"))
    plt.show()
