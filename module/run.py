#!/usr/bin/env python3

# Imports
import re
import os
import requests


# Constants
DESCRIPTION_PATH = "/Users/rohan/desktop/IT-Certification-Final-Project/supplier-data/description/"
IMAGE_PATH = "/Users/rohan/desktop/IT-Certification-Final-Project/supplier-data/images/"

# Functions
def convert_to_json():
  """
  Converts data to json dictionary
  """

  url = "http://[linux-instance-external-IP]/fruits"
  
  # Get all files in the description folder
  folder = os.listdir(DESCRIPTION_PATH)
 
  # Loop through all files in the folder
  for files in folder:
    # Open each file for reading
    with open(DESCRIPTION_PATH + files, 'r') as txt_file:
      # Read contents of file
      lines = txt_file.readlines()
  
      # Create the dictionary with data 
      data = {"name": lines[0].strip(), "weight": int(lines[1].strip(" lbs\n")), "description": lines[2], "image_name": lines[0].strip() + ".jpg"}
      # Send the data to web server
      response = requests.send(url, json=data)
 
  
convert_to_json()  


