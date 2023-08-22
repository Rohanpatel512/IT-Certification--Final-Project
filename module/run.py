#!/usr/bin/env python3

# Imports
import re
import os
import requests


# Constants
DESCRIPTION_PATH = "/supplier-data/description/"
IMAGE_PATH = "/supplier-data/images/"

# Functions
def convert_to_json:
  """
  Converts data to json dictionary
  """
  
  # Local variables
  json_data = {}
  
  # Get all files in the description folder
  folder = os.listdir(DESCRIPTION_PATH)
 
  # Loop through all files in the folder
  for files in folder:
    # Open each file for reading
    with open(DESCRIPTION_PATH + files, 'r') as txt_file:
      
  
  


