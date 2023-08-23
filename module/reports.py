#!/usr/bin/env python3

# Imports
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Functions
def generate_report(filename, title, additional_info):
  # Create the sample style sheet object
  styles = getSampleStyleSheet()
 
  # Set the name of the PDF file
  report = SimpleDocTemplate(filename)
  
  # Set the title of the PDF file
  report_title = Paragraph(title, styles["h1"])
  
  # Add the information into file
  report_info = Paragraph(additional_info, styles["BodyText"])
	
  # Build the report
  report.build([report_title, report_info])
  
  # Return the pdf report
  return report;
 
    
