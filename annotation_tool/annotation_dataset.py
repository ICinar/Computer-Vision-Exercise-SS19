from __future__ import division
from tkinter import *
from PIL import Image, ImageTk
import os
import sys
import glob
import random
import cv2 as cv
import numpy as np
import math

fac = 1.5
def detect(img):
    #Groeße des Bilds verkleinern
    res = cv.resize(img, None, fx=fac, fy=fac, interpolation=cv.INTER_CUBIC)

    #Bild in Graustufen und Gauß-Filter anwenden
    gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

    #Canny-Algorithmus
    edged = cv.Canny(gray, 10,25)
    return edged




def drawBoundingBox(img):
    im2, cnts, hier = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # sortiere die Konturen nach groeße
    biggestC = max(cnts, key = cv.contourArea)
    largest_area = 0
    largest_i = 0
    i = 0
    for cnt in cnts:
        area = cv.contourArea(cnt)
        if (area > largest_area):
            largest_area = area
            largest_i = i
        i = i+ 1
    #cntsSorted = sorted(cnts, key=lambda z: cv.contourArea(z))
    #zeichne eine Bounding box
    x, y, w, h = cv.boundingRect(cnts[i-1])

    return x,y,w,h

def drawBoundingBox2(img):
    cnts, hier = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
     #sortiere die Konturen nach groeße
    cntsSorted = sorted(cnts, key=lambda x: cv.contourArea(x))
    x, y, w, h = cv.boundingRect(cntsSorted[len(cntsSorted) - 1])  #zeichne eine Bounding box
    return x, y, w, h


#write classes and bounding box points in a new created text file
def writeTxtFile(cl,x1,y1,w1,h1,img,path):
	labelname = img + '.txt'
	pf = path+"/"+img
	exists = os.path.isfile(pf)
	stat = "..."
	if exists:
		stat= "a+"
	else:
		stat= "w+"
	f = open(labelname,stat)
	
	f.write(str(cl))			#Classes
	f.write(" ")
	f.write(str(x1))			#First point
	f.write(" ")
	f.write(str(y1))			#Second point
	f.write(" ")
	f.write(str(w1))			#third point
	f.write(" ")
	f.write(str(h1))			#fourth point
	f.write("\n")
	f.close()

# overwrite the image with bounding box
def overwriteImage(name,img):
	cv.imwrite(name,img)

#check if path is a image
def check_image_with_pil(path):
    try:
        Image.open(path)
    except IOError:
        return False
    return True
  	
	
def convert(x,y,w,h,width,height):
	xmin = x
	xmax = w
	ymin = y
	ymax = h
	dw = 1./width
	dh = 1./height
	x2 = (xmin + xmax)/2.0
	y2 = (ymin +ymax)/2.0
	w2 = xmax - xmin
	h2 = ymax- ymin
	x2 = x2*dw
	w2 = w2*dw
	y2 = y2*dh
	h2 = h2*dh
	return (x2,y2,w2,h2)	
	
	
#-------------------MAIN------------------------------


pfad = input("Pfad mit Bilder: ")
files = []
#list all files in path
for r, d, f in os.walk(pfad):
	for file in f:
		files.append(os.path.join(r, file))
cl = input("Schlüsselarten(0=Auto,1=Haus,2=Briefkasten,3=Sonstiges): ")
#check all pictures and do a bounding box 
for f in files:
	if check_image_with_pil(f):
		bild = cv.imread(f)
		edged = detect(bild)
		kernel = np.ones((3, 3), np.uint8)
		closing = cv.morphologyEx(edged, cv.MORPH_CLOSE, kernel)
		closing = cv.resize(closing, None, fx=1/fac, fy=1/fac, interpolation=cv.INTER_CUBIC)
		x, y, w, h = drawBoundingBox2(closing)
		print ("X: ",x," Y: ",y," W: ",w," H: ",h," ",pfad[0])
		color = (0, 0, 255)
		cv.rectangle(bild, (x, y), (x+w, y+h), color, 2)
		height,width = bild.shape[:2]
		x2,y2,w2,h2 = convert(x,y,w,h,width,height)
		writeTxtFile(cl,x2,y2,w2,h2,os.path.splitext(f)[0],pfad)
		overwriteImage(f,bild)
		cv.imshow("Image",bild)
		cv.waitKey(0)
		cv.destroyAllWindows()