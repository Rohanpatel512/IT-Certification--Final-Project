#!/usr/bin/env python3

# Imports
import os
import datetime
import reports
import emails


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
  
  pdf_list = ["/Users/rohan/desktop/IT-Certification-Final-Project/tmp/processed.pdf", title, body_text]
  return pdf_list

if __name__ == '__main__':

   # Generate the pdf given the fruit data
   pdf_list = generate_pdf("/Users/rohan/desktop/IT-Certification-Final-Project/supplier-data/description/")
   
   # Generate the pdf report
   reports.generate_report(pdf_list[0], pdf_list[1], pdf_list[2])
   
   # Store all email information in variables 
   sender = "automation@example.com"
   recipient = "{}@example.com".format(os.environ['USER'])
   subject = "Upload Complete - Online Fruit Store"
   body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."   
   
   
   # Generate the email
   mail = emails.generate_email(sender, recipient, subject, body, "/Users/rohan/desktop/IT-Certification-Final-Project/tmp/processed.pdf")
   
   print(mail)

   """
   # Send the mail
   emails.send_email(mail)
   """
   
