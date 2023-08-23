#!/usr/bin/env python3

# Imports
import os
import datetime
import reports
from email.message import EmailMessage
import mimetypes
import smtplib


# Functions
def get_date():
  """
  Helper method to get the current date  
  """
  date = datetime.datetime.now()
  today = date.strftime("%B") + " " + date.strftime("%d") + ", " + date.strftime("%Y")
  return today


def generate_pdf(path):

  # Local variables
  body_text = ""  

  # Get all files in the path
  files = os.listdir(path)
 
  # Loop through file in the folder  
  for txt_file in files:
    # Open the file for reading
    with open(path + txt_file, 'r') as file:
      lines = file.readlines()
      body_text += "name: {}<br/> weight: {}<br/><br/>".format(lines[0], lines[1])

  # Create the title for the report
  title = "Processed Update on {}".format(get_date())
  
  pdf_list = ["/tmp/processed.pdf", title, body_text]
  return pdf_list

if __name__ == '__main__':

   # Generate the pdf given the fruit data
   pdf_list = generate_pdf("/supplier-data/description/")
   
   # Generate the pdf report
   pdf_report = reports.generate_report(pdf_list[0], pdf_list[1], pdf_list[2])
    
   
      
