OFP Converter – README

0. About the program and me
The script is intended to be used for cross country flights. It converts all the data in a foreflight navlog to the OSM OFP. It does not fill out the second page of the OSM OFP per now.

This was made by WFO, I am not a programmer, and this was made with limited skill and chatGPT
There is no guarantee this script will work as intended, ALWAYS CROSS CHECK BEFORE USING.

If you run into problems, please contact me with the foreflight navlog at wfo.student@flyosm.com



1. Overview

This program converts a ForeFlight Navlog PDF into a filled-out OSM Aviation OFP (“Clean_OFP.pdf”) by extracting flight leg data and writing it into the correct fields.

Input:
Foreflight_OFP.pdf (ForeFlight Navlog)

Output:
Filled_OFP.pdf (completed flight plan)

The process uses simple PDF text extraction + coordinate-based text drawing.

The script only reads the first page of the Foreflight navlog.
This means that the navigational part of the Foreflight navlog with waypoints (excluding alternate) can not be more than one pages long!
If the list of waypoints carry over to the second page, this scrip will not work as intended!



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

OFP converter 1.x.py
Foreflight_OFP.pdf
Clean_OFP.pdf


Foreflight_OFP.pdf = ForeFlight Navlog exported as PDF

Clean_OFP.pdf = Empty OFP template

OFP converter 1.x.py = The conversion script

Additionaly, I have also left Template_OFP which is a totally empty OFP.



5. How to Run the Program

Open Command Prompt in the folder containing the script.

Run:

python "OFP converter 1.x.py"

You will be prompted to either press enter to continue, or enter a line number you want to delete.
What this does is it will delete the lines you enter. For example if you write 3, 6, 7. These lines will be deleted and not appear in Filled_OFP.pdf
This function is especially useful to delete waypoints you don't want in your OFP like Eivindstad, Uglebu or Ålefjær.
Lines like TOC, TOD, Stay and so on should be deleted automatically



6. Troubleshooting
Problem: “ModuleNotFoundError”

Open cmd and enter the following:

pip install pdfplumber reportlab pypdf pikepdf



8. Notes

The program currently can not input waypoint names, I suggest you fill this data into the OFP manually. Same with true track, variation and minimum fuel.

Extraction of data is automatically deteced only when the foreflight navlog is exported as pdf in the "Standard" format, Basic and International formats are not supported.



If something doesnt work and this document doesnt explain it properly, chatGPT probably can!