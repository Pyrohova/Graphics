import cv2
import numpy as np 
from matplotlib import pyplot as plt 

sobelImg = cv2.imread('img/sobel.jpg')

def getSobelX(img, size):
    sobelX = cv2.Sobel(img, -1, 1, 0, ksize = size)
    plt.imshow(sobelX)
    plt.show()

def getSobelY(img, size):
    sobelY = cv2.Sobel(img, -1, 0, 1, ksize = size)
    plt.imshow(sobelY)
    plt.show()

getSobelX(sobelImg, 5)
getSobelY(sobelImg, 5)
