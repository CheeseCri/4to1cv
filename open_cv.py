__author__= "yunghn3@gmail.com"

import cv2
import numpy
import matplotlib

count_image1 = 0
count_image2 = 0
count_image3 = 0
count_image4 = 0

#img
image1_xy = []
image2_xy = []
image3_xy = []
image4_xy = []

def input_image1(event, x, y, flags, param ):
    global count_image1
    if event == cv2.EVENT_LBUTTONDOWN:
        if(count_image1 < 3):
            count_image1 = count_image1 + 1
            print("(x,y) = ({},{})".format(x, y))
            image1_xy.append([x, y])

def input_image2(event, x, y, flags, param ):
    global count_image2
    if event == cv2.EVENT_LBUTTONDOWN:
        if(count_image2 < 3):
            count_image2 = count_image2 + 1
            print("(x,y) = ({},{})".format(x, y))
            image2_xy.append([x, y])

def input_image3(event, x, y, flags, param ):
    global count_image3
    if event == cv2.EVENT_LBUTTONDOWN:
        if(count_image3 < 3):
            count_image3 = count_image3 + 1
            print("(x,y) = ({},{})".format(x, y))
            image3_xy.append([x, y])

def input_image4(event, x, y, flags, param ):
    global count_image4
    if event == cv2.EVENT_LBUTTONDOWN:
        if(count_image4 < 3):
            count_image4 = count_image4 + 1
            print("(x,y) = ({},{})".format(x, y))
            image4_xy.append([x, y])

path_01 = "/Users/yungeontaeg/myworkspace/COMARTSYSTEM/Panorama/PanoramaProject/resource/01_new.jpg"
path_02 = "/Users/yungeontaeg/myworkspace/COMARTSYSTEM/Panorama/PanoramaProject/resource/02_new.jpg"
path_03 = "/Users/yungeontaeg/myworkspace/COMARTSYSTEM/Panorama/PanoramaProject/resource/03_new.jpg"
path_04 = "/Users/yungeontaeg/myworkspace/COMARTSYSTEM/Panorama/PanoramaProject/resource/04_new.jpg"

print("START")
image1 = cv2.imread(path_01, cv2.IMREAD_COLOR)
image1_resize = cv2.resize(image1, dsize=(0,0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
image2 = cv2.imread(path_02, cv2.IMREAD_COLOR)
image2_resize = cv2.resize(image2, dsize=(0,0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
image3 = cv2.imread(path_03, cv2.IMREAD_COLOR)
image3_resize = cv2.resize(image3, dsize=(0,0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
image4 = cv2.imread(path_04, cv2.IMREAD_COLOR)
image4_resize = cv2.resize(image4, dsize=(0,0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)



print("READ IMAGE")
cv2.namedWindow('01')
cv2.setMouseCallback('01', input_image1)
cv2.namedWindow('02')
cv2.setMouseCallback('02', input_image2)
cv2.namedWindow('03')
cv2.setMouseCallback('03', input_image3)
cv2.namedWindow('04')
cv2.setMouseCallback('04', input_image4)

print("NAMEDWINDOW")
cv2.imshow('01', image1_resize)
cv2.imshow('02', image2_resize)
cv2.imshow('03', image3_resize)
cv2.imshow('04', image4_resize)

print("IMSHOW")
cv2.waitKey(0)
print("WAITKEY")
cv2.destroyAllWindows()
print("DESTORYALLWINDOWS")

print(image1_xy)
print(image2_xy)
print(image3_xy)
print(image4_xy)

