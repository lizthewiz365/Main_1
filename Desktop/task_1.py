import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv


def rgb_image(original):
    image = cv2.imread(original)
    fig, ax = plt.subplots(1, 3, figsize=(15,5), sharey = True) 
    
    ax[0].imshow(image[:,:,0], cmap = 'Reds')
          
    ax[1].imshow(image[:,:,1], cmap = 'Greens')
   
    ax[2].imshow(image[:,:,2], cmap = 'Blues')    
    
    return


def hsv_image(original):
    image = cv2.imread(original)
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    fig, ax = plt.subplots(1, 3, figsize=(15,7), sharey = True)
    
    ax[0].imshow(img_hsv[:,:,0], cmap = 'hsv')
          
    ax[1].imshow(img_hsv[:,:,1], cmap = 'Greys')
   
    ax[2].imshow(img_hsv[:,:,2], cmap = 'gray')
    
    return



img = cv2.imread("doggy.jpg")
cv2.imshow("Doggo",img)
cv2.waitKey(0)
rgb_image("doggy.jpg")  
cv2.waitKey(0)
hsv_image("doggy.jpg")
    




