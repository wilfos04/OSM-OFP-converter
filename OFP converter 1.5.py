import pdfplumber
from reportlab.pdfgen import canvas
from pypdf import PdfReader
import io


with pdfplumber.open("Foreflight_OFP.pdf") as pdf:
    page = pdf.pages[0]
    words = page.extract_words(use_text_flow=False)


#Used to print a table of coordinates
"""
#prints all words in first table
for w in words:
    if w["text"].isalnum():
        print(w)
"""

"""
with pdfplumber.open("Test1.pdf") as pdf:
    page = pdf.pages[0]
    for w in page.extract_words():
        print(repr(w["text"]), w["x0"], w["x1"])
"""


#Examples I used to find coordiantes of data points
"""
'MAG' 147.0117 165.67729999999997
'WIND' 229.5984 250.9216
'SPD' 299.3446 315.79260000000005
'KT' 318.01660000000004 328.68219999999997
'DIST' 341.1129 359.3369
'NM' 361.5577 373.9993
'FUEL' 392.5418 413.4298
'G' 415.5106 421.7346
'TIME' 504.6516 523.7604
'WAYPOINT' 18.0 59.9392
'AIRWAY' 97.70432 128.83232
'HDG' 136.0426 153.8218
'CRS' 158.3922 175.28340000000003
'ALT' 187.0508 202.014
'CMP' 212.4176 230.1952
'DIR/SPD' 234.5317 266.97970000000004
'ISA' 275.582 288.9164
'TAS' 296.695 312.1046
'GS' 317.8457 329.4041
'LEG' 338.8398 355.2862
'REM' 358.4926 376.2702
'USED' 383.4805 405.7061
'REM' 412.7676 430.5452
'ACT' 447.8918 464.335
'LEG' 482.9461 499.3925
'REM' 506.9176 524.6952
'ETE' 529.4645 545.0229
'ACT' 565.6793 582.1225000000001
'ENGK' 18.0 45.2064
"""

"""
'MAG' 121.4742 140.13979999999998
'WIND' 207.1234 228.44660000000002
'SPD' 279.007 295.45500000000004
'KT' 297.67900000000003 308.34459999999996
'DIST' 322.3691 340.5931
'NM' 342.8139 355.2555
'FUEL' 374.9418 395.8298
'G' 397.9106 404.1346
'TIME' 496.0703 515.1791
'WAYPOINT' 18.0 59.9392
'AIRWAY' 70.59805 101.72605
'HDG' 110.0801 127.8593
'CRS' 133.3047 150.1959
'ALT' 162.907 177.8702
'CMP' 189.2426 207.02020000000002
'DIR/SPD' 212.5066 244.9546
'ISA' 254.3633 267.6977
'TAS' 276.0012 291.4108
'GS' 297.927 309.4854
'LEG' 319.7023 336.14869999999996
'REM' 340.1738 357.95140000000004
'USED' 366.0867 388.3123
'REM' 395.6988 413.4764
'ACT' 434.3043 450.7475
'LEG' 473.5149 489.9613
'REM' 498.3988 516.1764000000001
'ETE' 521.7957 537.3541
'ACT' 562.1043 578.5475
'ENGK' 18.0 45.2064
"""



#--------------------00000000000000--------------------------
#This section finds the X axis coordinates for navigational data in the foreflight OFP

for w in words:
    if w["text"] == "HDG" and w["top"] > 150:
        mhx0 = w["x0"] - 1
        mhx1 = w["x1"] + 1
        
    if w["text"] == "CRS" and w["top"] > 150:
        mtx0 = w["x0"] - 1
        mtx1 = w["x1"] + 1
        
    if w["text"] == "ALT" and w["top"] > 150:
        altx0 = w["x0"] - 7
        altx1 = w["x1"] + 7
        
    if w["text"] == "DIR/SPD" and w["top"] > 150:
        dsx0 = w["x0"] - 3
        dsx1 = w["x1"] + 3
        
    if w["text"] == "TAS" and w["top"] > 150:
        tasx0 = w["x0"] - 3
        tasx1 = w["x1"] + 3
        
    if w["text"] == "GS" and w["top"] > 150:
        gsx0 = w["x0"] - 3
        gsx1 = w["x1"] + 3
        
    if w["text"] == "LEG" and w["top"] > 150 and w["x0"] < 390:
        intdx0 = w["x0"] - 3
        intdx1 = w["x1"] + 3
        
    if w["text"] == "USED" and w["top"] > 150:
        usedx0 = w["x0"] - 3
        usedx1 = w["x1"] + 3
        
    if w["text"] == "LEG" and w["top"] > 150 and w["x0"] > 390:
        legtx0 = w["x0"] - 3
        legtx1 = w["x1"] + 3
        
    if w["text"] == "ETE" and w["top"] > 150:
        tottx0 = w["x0"] - 3
        tottx1 = w["x1"] + 3
    


        
        
#--------------------00000000000000--------------------------
#This section fills all the lists







#autofilling waypoints doesnt work yet

waypoints = []

for w in words:
    if 10 < w["x0"] < 80 and w["top"] > 220 and w["text"].isalnum():
        waypoints.append(w["text"])


used_legs = [0]
intf_legs = []
bottom = 1000

for w in words:
    if usedx0 < w["x0"] < usedx1 and w["top"] > 220:
        if w["text"] == "-":
            bottom = w["top"]
            break
        elif w["text"] == "ISA":
            bottom = w["top"]
            break
        used_legs.append(w["text"])

bottom -= 30


a = 1

while a < len(used_legs):
    if used_legs[a] == '-':
        used_legs[a] = 0
        intf_legs.append(0)
        a += 1
    else:
        intf_legs.append(round(float(used_legs[a]) - float(used_legs[a - 1]), 1))
        a += 1


#legacy code
ete_legs = []
"""
for w in words:
    if legtx0 < w["x0"] < legtx1 and w["top"] > 220 and w["top"] < bottom:
        ete_legs.append(w["text"])"""


tot_legs = []

for w in words:
    if tottx0 < w["x0"] < tottx1 and w["top"] > 220 and w["top"] < bottom:
        tot_legs.append(w["text"])


alt_legs = []

for w in words:
    if altx0 < w["x0"] < altx1 and w["top"] > 220 and w["top"] < bottom:
        alt_legs.append(w["text"])





kts_legs = []
dir_legs = []
winds = []

for w in words:
    if dsx0 < w["x0"] < dsx1 and w["top"] > 220 and w["top"] < bottom:
        winds.append(w["text"])

for w in winds:
    if w == '-':
        dir_legs.append('-')
        kts_legs.append('-')
        continue
    d, s = w.split("/")
    dir_legs.append(d)
    kts_legs.append(int(s))



tas_legs = []

for w in words:
    if tasx0 < w["x0"] < tasx1 and w["top"] > 220 and w["top"] < bottom:
        tas_legs.append(w["text"])


gs_legs = []

for w in words:
    if gsx0 < w["x0"] < gsx1 and w["top"] > 220 and w["top"] < bottom:
        gs_legs.append(w["text"])


mt_legs = []

for w in words:
    if mtx0 < w["x0"] < mtx1 and w["top"] > 220 and w["top"] < bottom:
        mt_legs.append(w["text"])



mh_legs = []

for w in words:
    if mhx0 < w["x0"] < mhx1 and w["top"] > 220 and w["top"] < bottom:
        mh_legs.append(w["text"])
        
        

wca_legs = []
i = 0

while i < len(mt_legs):
    if mh_legs[i].isdigit() and mt_legs[i].isdigit():
        if int(mh_legs[i]) - int(mt_legs[i]) > 40:
            pass
            wca_legs.append((int(mh_legs[i]) - int(mt_legs[i])) - 360)
        elif int(mh_legs[i]) - int(mt_legs[i]) < -40:
            pass
            wca_legs.append((int(mh_legs[i]) - int(mt_legs[i])) + 360)    
            
        else:
            wca_legs.append(int(mh_legs[i]) - int(mt_legs[i]))
        i += 1
    else:
        wca_legs.append("-")
        i += 1


int_legs = []

for w in words:
    if intdx0 < w["x0"] < intdx1 and w["top"] > 220 and w["top"] < bottom:
        if w["text"] == "-":
            int_legs.append("0")
        else: 
            int_legs.append(w["text"])
        


totd_legs = []
totd_legs.append(int_legs[0])

j = 1
while j < len(int_legs):
    totd_legs.append(int(int_legs[j]) + int(totd_legs[j - 1]))
    j += 1











#--------------------00000000000000--------------------------

#this section deletes all TOC, TOD and extra unnaccesary spaces from the foreflight format

#ADD NUMBERS TO THE BLACKLIST IF YOU WANT TO DELETE LINES
#Example:
#Type into the scratchpad when running eg. "7" then enter, "9" then enter to delete lines 7 and 9
    
blacklist = []


print("Press enter to continue, or enter a line number you want to delete")
userinput = input()


while userinput != "":
    blacklist.append(int(userinput))
    print("Line", userinput, "will be skipped")
    userinput = input()


#This code will delete a segment if the track is the same for to lines,
#Or if the TAS = 0 or if the track is only a dash "-"
b = 0
while b < len(mt_legs) - 1:
    if mt_legs[b + 1] == mt_legs[b]:
        blacklist.append(b)
        
    elif tas_legs[b] == "0":
        blacklist.append(b)
        
    elif mt_legs[b] == "-":
        blacklist.append(b)
        
    
    b += 1


        
#The blacklist is a list filled with the index numbers of the lines to be deleted
#it is sorted and prepared, in the "for" loop they are deleted

blacklist.sort()

blacklist.reverse()

int_legs.append(0)
intf_legs.append(0)


for c in blacklist:
    z = 0
    while z < len(alt_legs):
        
        if z == c:
            
            waypoints.pop(z)
            
            alt_legs.pop(z)
            
            dir_legs.pop(z)
            
            kts_legs.pop(z)
            
            tas_legs.pop(z)
            
            gs_legs.pop(z)
            
            mt_legs.pop(z)
            
            wca_legs.pop(z)
            
            mh_legs.pop(z)

            int_legs[z + 1] = int(int_legs[z]) + int(int_legs[z + 1])
            int_legs.pop(z)
             
            totd_legs.pop(z)
            
            #legacy code
            """if z >= 1:
               
                ete1 = int(ete_legs[z][0])
                ete2 = int(ete_legs[z][2]) 
                ete3 = int(ete_legs[z][3])
                
                ete4 = int(ete_legs[z + 1][0])
                ete5 = int(ete_legs[z + 1][2])
                ete6 = int(ete_legs[z + 1][3])
                
                
                ete_legs[z + 1] = str(ete1 + ete4) + ":" + str(ete2 + ete5) + str(ete3 + ete6)
            
            
            ete_legs.pop(z)"""
            
            tot_legs.pop(z)
            
            
            
            intf_legs[z + 1] = round(intf_legs[z + 1] + intf_legs[z], 2)
            intf_legs.pop(z)
            
        z += 1

int_legs.pop(len(int_legs)-1)
intf_legs.pop(len(intf_legs)-1)




#This section fills the ETE time, it is done by subtracting the previous total time

r = 0
while r < len(tot_legs):
    
    n0 = tot_legs[r][0]
    n1 = tot_legs[r][1]
    n2 = tot_legs[r][2]
    n3 = tot_legs[r][3]
    
    #First ETE leg is the same as TOT time
    if r == 0:
        if n2 == "0":
            ete_legs.append(n3)
        else:
            ete_legs.append(n2 + n3)
        
    #ETE is an easy subtraction if its still within the first hour (first number is 0)
    elif n0 == "0":
        nx = int(n2 + n3)
        ny = nx - int(tot_legs[r-1][2] + tot_legs[r-1][3])
        ete_legs.append(ny)
        
    #A bit more complex when you get into the second or third hour of flight
    elif n0 != "0":
        nx = int(n2 + n3)
        ny = nx - int(tot_legs[r-1][2] + tot_legs[r-1][3])
        
        if ny >= 0:
            
            #in case ETE is more than one hour
            if n0 != tot_legs[r-1][0]:
                
                if len(str(ny)) == 2:
                    ete_legs.append("1:" + str(ny))
                    
                else:
                    ete_legs.append("1:0" + str(ny))
                
            else:
                ete_legs.append(ny)
                
        #If the current total time (only the minutes) minus the previous minutes returns
        #negative minutes, this section adresses that and adds 60
        elif ny < 0:
            ny += 60
            
            #in case TOT jumps 2 hour marks eg. 0:xx -> 2:xx
            if n0 != str(int(tot_legs[r-1][0]) + 1):
                
                if len(str(ny)) == 2:
                    ete_legs.append("1:" + str(ny))
                    
                else:
                    ete_legs.append("1:0" + str(ny))
                
            else:
                ete_legs.append(ny)
                
        
    r += 1
    




#--------------------00000000000000--------------------------
#This section draws all the data into the first page OFP


x = 227
dx = 42
line_height = 27.3

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=(1200, 842))
can.setFont("Helvetica", 17)

"""
y = 344.2
for d in waypoints:
    can.drawString(25, y, d)
    if y < 70:
        break
    y -= line_height
"""
y = 470
"""for d in alt_legs:
    can.drawRightString(x, y, d)
    if y < 100:
        break
    y -= line_height"""

y = 470
for d in dir_legs:
    can.drawRightString(x + 2*dx, y, d)
    if y < 100:
        break
    y -= line_height

y = 470
for d in kts_legs:
    can.drawRightString(x + 3*dx, y, str(d))
    if y < 100:
        break
    y -= line_height

y = 470
for d in tas_legs:
    can.drawRightString(x + 4*dx, y, d)
    if y < 100:
        break
    y -= line_height

y = 470
for d in gs_legs:
    can.drawRightString(x + 5*dx, y, d)
    if y < 100:  
        break
    y -= line_height

y = 470
for d in mt_legs:
    can.drawRightString(x + 8*dx, y, d)
    if y < 100:
        break
    y -= line_height

y = 470
for d in wca_legs:
    can.drawRightString(x + 9*dx, y, str(d))
    if y < 100:
        break
    y -= line_height
    
y = 470
for d in mh_legs:
    can.drawRightString(x + 10*dx, y, d)
    if y < 100:
        break
    y -= line_height
    
y = 470
for d in int_legs:
    can.drawRightString(x + 11*dx, y, str(d))
    if y < 100:
        break
    y -= line_height
    
y = 470
for d in totd_legs:
    can.drawRightString(x + 12*dx, y, str(d))
    if y < 100:
        break
    y -= line_height

y = 470
for d in ete_legs:
    can.drawRightString(x + 13*dx, y, str(d))
    if y < 100:
        break
    y -= line_height

y = 470
for d in tot_legs:
    can.drawRightString(x + 14*dx, y, d)
    if y < 100:
        break
    y -= line_height

y = 470
for d in intf_legs:
    can.drawRightString(x + 19*dx, y, str(d))
    if y < 100:
        break
    y -= line_height




#writes the new PDF file
can.save()
packet.seek(0)


overlay = PdfReader(packet)
template = PdfReader("Clean_OFP.pdf")



# ---- NEW MERGE LOGIC (PIKEPDF) ----
import pikepdf

packet.seek(0)

# Open the base OFP template (keeps all form fields intact)
base_pdf = pikepdf.Pdf.open("Clean_OFP.pdf")

# Open the overlay generated by reportlab
overlay_pdf = pikepdf.Pdf.open(packet)

# Apply overlay on page 0
page = base_pdf.pages[0]
page.add_overlay(overlay_pdf.pages[0])

# Save output
base_pdf.save("Filled_OFP.pdf")
# -----------------------------------

print("Completed, Filled_OFP.pdf has been updated")
    


