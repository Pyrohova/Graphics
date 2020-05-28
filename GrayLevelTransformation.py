from PIL import Image
from pylab import *

grayImage = Image.open('img/grayTransform.jpg')

def getNegative(img) :
    transformed = 255 - array(img)
    result = Image.fromarray(transformed)
    result.show()

def getClampedToInterval(img, start, end):
    transformed = ((end - start / 255) * array(img) + start).astype(np.uint8)
    result = Image.fromarray(transformed)
    result.show()

def getDarker(img, degree):
    transformed = (255.0 * (array(img) / 255.0) ** degree).astype(np.uint8)
    result = Image.fromarray(transformed)
    result.show()

grayImage.show()
getNegative(grayImage)
getClampedToInterval(grayImage,100,200)
getDarker(grayImage,2)