import pdfplumber
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
import io


with pdfplumber.open("Foreflight_OFP.pdf") as pdf:
    page = pdf.pages[0]
    words = page.extract_words(use_text_flow=False)

"""
#prints all words in first table
for w in words:
    if w["text"].isalnum():
        print(w)
"""
"""

with pdfplumber.open("Foreflight_OFP.pdf") as pdf:
    page = pdf.pages[0]
    for w in page.extract_words():
        print(repr(w["text"]), w["x0"], w["x1"])
"""



        
        
#--------------------00000000000000--------------------------
#This section fills all the lists







#autofilling waypoints doesnt work yet, which is why it is commented below

"""waypoints = []

for w in words:
    if 17 < w["x0"] < 80 and w["top"] > 220 and w["text"].isalnum():
        waypoints.append(w["text"])
"""

used_legs = [0]
intf_legs = []
bottom = 0

for w in words:
    if 370 < w["x0"] < 395 and w["top"] > 220:
        if w["text"] == "-":
            bottom = w["top"]
            break
        elif w["text"] == "ISA":
            bottom = w["top"]
            break
        used_legs.append(w["text"])

bottom -= 20



a = 1

while a < len(used_legs):
    if used_legs[a] == '-':
        used_legs[a] = 0
        intf_legs.append(0)
        a += 1
    else:
        intf_legs.append(round(float(used_legs[a]) - float(used_legs[a - 1]), 1))
        a += 1



ete_legs = []

for w in words:
    if 473 < w["x0"] < 496 and w["top"] > 220 and w["top"] < bottom:
        ete_legs.append(w["text"])


tot_legs = []

for w in words:
    if 520 < w["x0"] < 542 and w["top"] > 220 and w["top"] < bottom:
        tot_legs.append(w["text"])


alt_legs = []

for w in words:
    if 170 < w["x0"] < 195 and w["top"] > 220 and w["top"] < bottom:
        alt_legs.append(w["text"])





kts_legs = []
dir_legs = []
winds = []

for w in words:
    if 220 < w["x0"] < 260 and w["top"] > 220 and w["top"] < bottom:
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
    if 284 < w["x0"] < 301 and w["top"] > 220 and w["top"] < bottom:
        tas_legs.append(w["text"])


gs_legs = []

for w in words:
    if 303 < w["x0"] < 320 and w["top"] > 220 and w["top"] < bottom:
        gs_legs.append(w["text"])


mt_legs = []

for w in words:
    if 149 < w["x0"] < 166 and w["top"] > 220 and w["top"] < bottom:
        mt_legs.append(w["text"])



mh_legs = []

for w in words:
    if 123 < w["x0"] < 140 and w["top"] > 220 and w["top"] < bottom:
        mh_legs.append(w["text"])
        

        

wca_legs = []
i = 0

while i < len(mt_legs):
    if mh_legs[i].isdigit() and mt_legs[i].isdigit():
        if int(mh_legs[i]) - int(mt_legs[i]) > 40:
            pass
            wca_legs.append((int(mh_legs[i]) - int(mt_legs[i])) - 360)
        else:
            wca_legs.append(int(mh_legs[i]) - int(mt_legs[i]))
        i += 1
    else:
        wca_legs.append("-")
        i += 1


int_legs = []

for w in words:
    if 328 < w["x0"] < 341 and w["top"] > 220 and w["top"] < bottom:
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
#ADD NUMBERS TO THE BLACKLIST IF YOU WANT TO DELETE LINES EG.: [3, 8]
    
blacklist = []


print("Press enter to continue, or enter line numbers you want to delete in list format eg.: 5, 8")
userinput = input()
if userinput != '':
    blacklist.append(int(userinput))

b = 0
while b < len(mt_legs) - 1:
    if mt_legs[b + 1] == mt_legs[b]:
        blacklist.append(b)
    elif mt_legs[b] == "-":
        blacklist.append(b)
    elif True:
        pass
    b += 1


        


blacklist.sort()

blacklist.reverse()

int_legs.append(0)
intf_legs.append(0)


for c in blacklist:
    z = 0
    while z < len(alt_legs):
        
        if z == c:
            #waypoints.pop(z)
            
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
            
            ete_legs.pop(z)
            
            tot_legs.pop(z)
            
            intf_legs[z + 1] = round(intf_legs[z + 1] + intf_legs[z], 2)
            intf_legs.pop(z)
            
        z += 1

int_legs.pop(len(int_legs)-1)
intf_legs.pop(len(intf_legs)-1)


"""
badwaypoints = ["GKMJA", "CNGRE", "CNALE", "GKRYK", "CNRAM", "Stay"]
waypoints = [x for x in waypoints if x not in badwaypoints]"""

#--------------------00000000000000--------------------------
#This section draws all the data into the first page OFP


x = 0
dx = 30

y = 335
line_height = 19.2

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=(1000, 842))

"""
y = 344.2
for d in waypoints:
    can.drawString(25, y, d)
    if y < 70:
        break
    y -= line_height
"""
y = 335
for d in alt_legs:
    can.drawRightString(160, y, d)
    if y < 70:
        break
    y -= line_height

y = 335
for d in dir_legs:
    can.drawRightString(220, y, d)
    if y < 70:
        break
    y -= line_height

y = 335
for d in kts_legs:
    can.drawRightString(250, y, str(d))
    if y < 70:
        break
    y -= line_height

y = 335
for d in tas_legs:
    can.drawRightString(280, y, d)
    if y < 70:
        break
    y -= line_height

y = 335
for d in gs_legs:
    can.drawRightString(308, y, d)
    if y < 70:  
        break
    y -= line_height

y = 335
for d in mt_legs:
    can.drawRightString(395, y, d)
    if y < 70:
        break
    y -= line_height

y = 335
for d in wca_legs:
    can.drawRightString(425, y, str(d))
    if y < 70:
        break
    y -= line_height
    
y = 335
for d in mh_legs:
    can.drawRightString(455, y, d)
    if y < 70:
        break
    y -= line_height
    
y = 335
for d in int_legs:
    can.drawRightString(480, y, str(d))
    if y < 70:
        break
    y -= line_height
    
y = 335
for d in totd_legs:
    can.drawRightString(510, y, str(d))
    if y < 70:
        break
    y -= line_height

y = 335
for d in ete_legs:
    can.drawRightString(542, y, d)
    if y < 70:
        break
    y -= line_height

y = 335
for d in tot_legs:
    can.drawRightString(572, y, d)
    if y < 70:
        break
    y -= line_height

y = 335
for d in intf_legs:
    can.drawRightString(722, y, str(d))
    if y < 70:
        break
    y -= line_height




#writes the new PDF file
can.save()
packet.seek(0)

overlay = PdfReader(packet)
template = PdfReader("Clean_OFP.pdf")

writer = PdfWriter()
page = template.pages[0]
page2 = template.pages[1]
page.merge_page(overlay.pages[0])
writer.add_page(page)
writer.add_page(page2)

with open("Filled_OFP.pdf", "wb") as f:
    writer.write(f)

print("Completed, Filled_OFP has been updated")
    


