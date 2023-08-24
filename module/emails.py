#!/usr/bin/env python3

# Imports
from email.message import EmailMessage
import mimetypes
import os
import smtplib

# Functions
def generate_email(sender, recipient, subject, body, pdf):

  # Create an instance of the email message 
  mail = EmailMessage()
  
  # Set the To, From, and Subject values
  mail['To'] = recipient
  mail['From'] = sender
  mail['Subject'] = subject
  
  # Set the body of email
  mail.set_content(body)
 
  mime_type, _ = mimetypes.guess_type(pdf)
  mtype, stype = mime_type.split("/", 1)
  
  # Attach the pdf report to email
  with open(pdf, 'rb') as attachment_file:
    mail.add_attachment(attachment_file.read(), maintype=mtype, subtype=stype, filename=os.path.basename(pdf))

  # Return the mail
  return mail

def generate_error_report(sender, recipient, subject, body):
  
  # Create an instance of the email message
  mail = EmailMessage()
  
  # Set the To, From, and Subject values
  mail['To'] = recipient
  mail['From'] = sender
  mail['Subject'] = subject
 
  # Set the body of email
  mail.set_content(body)
  
  # Return the mail
  return mail
  

def send_email(mail):
  
  # Connect to the local machine 
  mail_server = smtplib.SMTP('localhost') 

  # Send the email 
  mail_server.send_message(mail)
	
  # Close the connection to mail server
  mail_server.quit()
