#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 23:59:17 2022

@author: piyush
"""


##################resize image###########

import os, sys
from PIL import Image

filepath = "/home/piyush/PDF_MERGE/"

img_fol = "img/"

#change size of output file  
size = 800, 1000

for infile in os.listdir(filepath+img_fol) :
        try:
            im = Image.open(filepath+img_fol+infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(filepath+img_fol+infile, "JPEG")
        except IOError:
            print("cannot create thumbnail for infile")


################################


###################convert img to pdf
from fpdf import FPDF

filepath = "/home/piyush/PDF_MERGE/"

img_fol = "img/"

pdf_fol = "out/"
# storing image path
pdf_file = "output.pdf"
  
# storing pdf path
pdf_path = filepath + pdf_file

pdf = FPDF()

imagelist = os.listdir(filepath+img_fol)


for image in imagelist:
    n = image.split('.')[0]
    os.rename(filepath+img_fol+image,filepath+img_fol+n)

#imagelist.sort()
imagelist = os.listdir(filepath+img_fol)

dt = [int(n) for n in imagelist]
dt.sort()

#imagelist is the list with all image filenames
for i in dt:    
    x=0
    y=0
    w=210   #For A4 size page 
    h=297
    l = filepath+img_fol+str(i)
    #c = l.split('.')
    #print(c)
    #if c.len() < 2:
    #os.rename(l,l+".jpg")
    pdf.add_page()
    pdf.image(l+".jpg",x,y,w,h)
    print(l+".jpg")
pdf.output(pdf_path, "F")    
##############################
