#!/usr/bin/env python3

# Imports
import os
import requests

# Functions
def upload_images():
  """
  Uploads all modified images in directory to web server
  """  

  # Local variables 
  url = "http://localhost/upload/"
  path = "supplier-data/images/"  

  # Loop through all the files in the directory
  for images in os.listdir(PATH):
    
    # Check if file is a .jpg file
    if images.endswith('.jpeg'): 
      # Open the image 
      with open(PATH + images, 'rb') as image:
        # Send the modified image to web server
        post_request = requests.post(url, files={'file': image})
      
upload_images()
 
