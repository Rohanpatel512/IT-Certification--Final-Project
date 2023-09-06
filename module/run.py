#!/usr/bin/env python3

# Imports
import re
import os
import requests


# Variables
url = "http://localhost/fruits/"
path = "supplier-data/descriptions/"


# Functions
def convert_to_json():
  """
  Converts data to json dictionary
  """
  
  # Get all files in the description folder
  folder = os.listdir(path)
 
  # Loop through all files in the folder
  for files in folder:
    # Open each file for reading
    with open(path + files, 'r') as txt_file:
      # Read contents of file
      lines = txt_file.readlines()
  
      # Create the dictionary with data 
      data = {"name": lines[0].strip(), "weight": int(lines[1].strip(" lbs\n")), "description": lines[2], "image_name": files.strip('.txt') + ".jpeg"}
      # Send the data to web server
      response = requests.post(url, json=data)
 
  
convert_to_json()  


