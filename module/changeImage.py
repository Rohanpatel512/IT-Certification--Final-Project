#!/usr/bin/env python3

# Imports
import os
import re
from PIL import Image

# Constants
SAVE_PATH = "supplier-data/images/"

def change():
 """
 Modifies each image in directory and then saves the image in the
 same directory.
 """

 # Get the list of images in the directory
 folder = os.listdir("supplier-data/images/")
 
 # Loop through all images in the folder
 for image_name in folder:

   if image_name != ".DS_Store" and '.tiff' in image_name:
     
     # Open each image
     image = Image.open("supplier-data/images/" + image_name)
    
     # Convert the image to a RGB 3-channel format
     modified_image = image.convert('RGB')
   
     # Resize the image to 600x400 pixel
     modified_image = modified_image.resize((600, 400))

     # Converts from .tiff to .jpg
     image_name = re.sub(r'.tiff', r'.jpeg', image_name)

     # Set the new path of formatted image
     directory = os.path.join(SAVE_PATH, image_name)
     
     # Save the formatted image to path
     modified_image.save(directory, "JPEG")
   
change()
    
    
 
 
