#!/usr/bin/env python3

# Imports
import os
import requests

# Constants
PATH = "/supplier-data/images/"

# Functions
def upload_images():
  """
  Uploads all modified images in directory to web server
  """  

  # Local variables 
  url = "[linux-instance-IP-Address]/upload"
 
  # Loop through all the files in the directory
  for images in os.listdir(PATH):
    
    # Check if file isn't a .DS_Store file
    if images != ".DS_Store": 
      # Open the image 
      with open(PATH + images, 'rb') as image:
        # Send the modified image to web server
        post_request = requests.post(url, files={'file': image})
      
      
 
