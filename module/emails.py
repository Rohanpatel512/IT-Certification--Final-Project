#!/usr/bin/env python3

# Imports
from email.message import EmailMessage
import mimetypes
import os
import smtplib

# Functions
def generate_email(pdf):
  
  # Local variables
  sender = "automation@example.com"
  recipient = "username@example.com"
  subject = "Upload Complete - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  # Create an instance of the email message 
  mail = EmailMessage()
  
  # Set the To, From, and Subject values
  mail['To'] = recipient
  mail['From'] = sender
  mail['Subject'] = subject
 
  mime_type, _ = mimetypes.guess_type(pdf)
  mtype, stype = mime_type.split("/", 1)
    
