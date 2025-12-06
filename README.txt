OFP Converter – README



1. Overview

This program converts a ForeFlight Navlog PDF into a filled-out OSM Aviation OFP (“Clean_OFP.pdf”) by extracting flight leg data and writing it into the correct fields.

Input:

Foreflight_OFP.pdf (ForeFlight Navlog)

Output:

Filled_OFP.pdf (completed flight plan)

The process uses simple PDF text extraction + coordinate-based text drawing.

You can not edit any of the fields in  Filled_OFP.pdf!! You can however edit Clean_OFP with the text fields you want, then run it through the script.
Any changes done to Clean_OFP.pdf will carry over after running the script!



2. Requirements

This program requires Python 3.10 or newer.

The following Python libraries must be installed:

Library	Purpose
pdfplumber	Read/parse text from PDFs
reportlab	Write text onto PDF canvas
pypdf	Merge overlay canvas with template PDF



3. Installation Instructions (Fresh Computer)
Step 1 — Install Python

Download and install Python from:

https://www.python.org/downloads/

During installation:

Check "Add Python to PATH"

Choose “Install for all users” if available

Verify installation:

python --version

Should return Python 3.X.X.



Step 2 — Install Required Python Packages

Open Command Prompt and run:

pip install pdfplumber
pip install reportlab
pip install pypdf



4. Files Needed in the Same Folder

Place the following files in one folder:

OFP converter 1.0.py
Foreflight_OFP.pdf
Clean_OFP.pdf


Foreflight_OFP.pdf = ForeFlight Navlog exported as PDF

Clean_OFP.pdf = Empty OFP template

OFP converter 1.0.py = The conversion script



5. How to Run the Program

Open Command Prompt in the folder containing the script.

Run:

python "OFP converter 1.0.py"

You will be prompted to either press enter, or to enter enter values into the "blacklist",
What this does is it will delete the lines you enter. Fore example if you write 3, 6, 7. These lines will be deleted and nott appear in Filled_OFP.pdf
This function is especially useful to delete waypoints you dont want in your OFP like Eivindstad, Uglebu or Ålefjær



6. Troubleshooting
Problem: “ModuleNotFoundError”

Open anaconda prompt and enter the following:

pip install pdfplumber reportlab pypdf



8. Notes

The program currently can not input waypoint names, I suggest you fill this data into Clean_OFP.pdf manually before running the script as this will carry over.

Extraction of data is based specifically tuned to the columns in the foreflight navlog by looking within X values (laterally along the document)
If ForeFlight changes its PDF layout, the program will no longer work and x-ranges will need updating.



If something doesnt work and this document doesnt explain it properly, chatGPT probably can!