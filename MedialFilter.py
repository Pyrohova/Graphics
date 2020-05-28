import scipy.misc
import scipy.ndimage

from PIL import Image

noiseImage = Image.open('img/noisy.png')

def getMedialFiltred(img,size) :
    transformed = scipy.ndimage.filters.median_filter(img, size=size, footprint= None, output=None, mode='reflect', cval=0.0, origin=0)
    result = Image.fromarray(transformed)
    result.show()

noiseImage.show()
getMedialFiltred(noiseImage,5)
