#!/usr/bin/env python3

# Imports
import os
import socket
import shutil
import psutil
import emails

# Constants
CPU_PERCENTAGE = 80
DISK_SPACE = 20
MEMORY = 500

# Variables
sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ['USER'])
body = "Please check your system and resolve the issue as soon as possible."

def email_report(subject):
  """
  Helper method used to generate the report given a subject
  and send the email
  """
   
  # Generate the error report email
  error_mail = emails.generate_error_report(sender, recipient, subject, body)  
  # Send the mail
  emails.send_mail(error_mail)

# Functions
def check_cpu_usage():
  """
  Checks if CPU usage is over 80%, if 
  usage is greater, it reports an error
  """

  # Local variables
  subject = "Error - CPU usage is over 80%"

  # Get the cpu usage
  cpu_usage = psutil.cpu_percent(interval=1)
  
  # Check if CPU usage is over 80% 
  if cpu_usage > CPU_PERCENTAGE:
    email_report(subject)


def check_disk_space():
  """
  Checks if disk space is lower than 20%.
  Reports an error if it is.
  """
  
  # Local variables
  subject = "Error - Available disk space is less than 20%"

  # Get the disk usage
  disk_usage = shutil.disk_usage('/')
   
  # Get the amount of disk space
  space = disk_usage.free / disk_usage.total
  space *= 100
  
  # Check if available disk space is less than or equal to 20%
  if space <= 20:
    email_report(subject)



def check_memory():
  """
  Checks if available memory is less than 500 MB
  and reports an error if it is.
  """
  
  # Local variables
  subject = "Error - Available memory is less than 500MB"
  
  # Get the available memory 
  available_memory = psutil.virtual_memory().available
  
  # Convert the available memory from bytes to megabytes
  available_memory_mb = available_memory / (1024**2)
  
  # Check if available memory is less than or equal to 500 MB
  if available_memory_mb <= MEMORY:
    email_report(subject)


 
def check_localhost():
  """
  Checks if localhost cannot be resolved to 
  127.0.0.1 and reports an error if this is the
  case.
  """
 
  # Local variables
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  
  # Get the hostname of local machine
  hostname = socket.gethostname()
  
  if hostname != "127.0.0.1":
    email_report(subject)



if __name__ == "__main__":
   check_cpu_usage()
   check_disk_space()
   check_memory()
   check_localhost()
   
