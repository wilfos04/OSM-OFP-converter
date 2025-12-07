OFP Converter – README

0. About the program and me
This was made by WFO, I do not really know how to program, I made this in a few days learning from chatGPT.
There is no guarantee this script will work, I barely know how python works, and am lucky to have gotten this script working
If you are more knowledgeable about this than me I recommend you to make your own version or improve this one!



1. Overview

This program converts a ForeFlight Navlog PDF into a filled-out OSM Aviation OFP (“Clean_OFP.pdf”) by extracting flight leg data and writing it into the correct fields.

Input:
Foreflight_OFP.pdf (ForeFlight Navlog)

Output:
Filled_OFP.pdf (completed flight plan)

The process uses simple PDF text extraction + coordinate-based text drawing.

The foreflight navigational part of the Foreflight OFP can not be more than one pages long!
If the waypoints carry over to the second page, this scrip will not work (alternate exempted, those wont be added to the OSM OFP)!



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
pip install pikepdf



4. Files Needed in the Same Folder

Place the following files in one folder:

OFP converter 1.3.py
Foreflight_OFP.pdf
Clean_OFP.pdf


Foreflight_OFP.pdf = ForeFlight Navlog exported as PDF

Clean_OFP.pdf = Empty OFP template

OFP converter 1.3.py = The conversion script



5. How to Run the Program

Open Command Prompt in the folder containing the script.

Run:

python "OFP converter 1.3.py"

You will be prompted to either press enter, or to enter enter values into the "blacklist",
What this does is it will delete the lines you enter. For example if you write 3, 6, 7. These lines will be deleted and not appear in Filled_OFP.pdf
This function is especially useful to delete waypoints you don't want in your OFP like Eivindstad, Uglebu or Ålefjær.
Lines like TOC, TOD, Stay and so on should be deleted automatically



6. Troubleshooting
Problem: “ModuleNotFoundError”

Open cmd and enter the following:

pip install pdfplumber reportlab pypdf pikepdf



8. Notes

The program currently can not input waypoint names, I suggest you fill this data into the OFP manually.

Extraction of data is automatically deteced only when the foreflight navlog is exported as pdf in the "Standard" format, Basic and International formats are not supported.



If something doesnt work and this document doesnt explain it properly, chatGPT probably can!