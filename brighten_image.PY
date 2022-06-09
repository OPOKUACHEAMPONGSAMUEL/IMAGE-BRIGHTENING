#import libraries needed for script
from PIL import Image,ImageEnhance 
#pillow for image manipulation

import glob 
#glob is used to read images in the specified directory

import numpy as np
#numpy aids in concatenating old and new images

#using glob library, read the lab images from folder
image_files = glob.glob(
    r'Images\*.*'
)

#create an array of the file paths of images
images = []

#create a loop to pick elements in image_files and add to new array
for image in image_files:
    images.append(image)
    
#loop the file paths to exclude directories in file paths to get only filename
for im in images:
    #use string.split attribute to read actual filename
    image_split = im.split('\\')
    image_name = image_split[1]
    
    #load image for enhancement
    imo = Image.open(im)
    enhancer = ImageEnhance.Brightness(imo)
    factor = 1.5 #gives original image
    im_bright = enhancer.enhance(factor)
    

    #save brightened image to directory
    im_bright.save(image_name + '_brightened.jpg')

    #display old and new image
    Image.fromarray(np.hstack((np.array(imo),np.array(im_bright)))).show()

