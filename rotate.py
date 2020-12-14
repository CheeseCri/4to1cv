__author__= "yunghn3@gmail.com"

import cv2
import numpy
import matplotlib
import math
import time

blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)

cv2.setUseOptimized(True)
print(cv2.useOptimized())

# image1_xy = [[536, 290], [347, 302], [112, 151]]
# # 상단 왼쪽
# image2_xy = [[58, 282], [245, 305], [530, 162]]
# # 상단 오른쪽
# image3_xy = [[542, 38], [537, 155], [354, 55]]
# # 하단 왼쪽
# image4_xy = [[63, 29], [56, 147], [247, 52]]
# 하단 오른쪽

screen_width = int(350 * 3.3)
screen_height = int(250 * 3.3)

count_image1 = 0
count_image2 = 0
count_image3 = 0
count_image4 = 0

image1_xy = []
image2_xy = []
image3_xy = []
image4_xy = []

def get_angle(arr):
    return math.degrees(math.atan2(arr[1][0]-arr[2][0], arr[1][1]-arr[2][1]))

def get_angle2(arr):
    return math.degrees(math.atan2(arr[1][1]-arr[2][1], arr[2][0]-arr[1][0]))

def input_image1(event, x, y, flags, param ):
    global count_image1
    if event == cv2.EVENT_LBUTTONDOWN:
        if(count_image1 < 3):
            count_image1 = count_image1 + 1
            print("(x,y) = ({},{})".format(x, y))
            image1_xy.append([x, y])
            if count_image1 == 3:
                cv2.line(image1, (image1_xy[0][0], image1_xy[0][1]), (image1_xy[0][0], image1_xy[0][1]), blue_color, 5)
                cv2.line(image1, (image1_xy[1][0], image1_xy[1][1]), (image1_xy[2][0], image1_xy[2][1]), blue_color, 5)

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
# image1_resize = cv2.resize(image1, dsize=(0,0), fx=1, fy=1, interpolation=cv2.INTER_AREA)
image2 = cv2.imread(path_02, cv2.IMREAD_COLOR)
# image2_resize = cv2.resize(image2, dsize=(0,0), fx=1, fy=1, interpolation=cv2.INTER_AREA)
image3 = cv2.imread(path_03, cv2.IMREAD_COLOR)
# image3_resize = cv2.resize(image3, dsize=(0,0), fx=1, fy=1, interpolation=cv2.INTER_AREA)
image4 = cv2.imread(path_04, cv2.IMREAD_COLOR)
# image4_resize = cv2.resize(image4, dsize=(0,0), fx=1, fy=1, interpolation=cv2.INTER_AREA)

cv2.namedWindow('01')
cv2.setMouseCallback('01', input_image1)
cv2.namedWindow('02')
cv2.setMouseCallback('02', input_image2)
cv2.namedWindow('03')
cv2.setMouseCallback('03', input_image3)
cv2.namedWindow('04')
cv2.setMouseCallback('04', input_image4)

print("NAMEDWINDOW")
cv2.imshow('01', image1)
cv2.imshow('02', image2)
cv2.imshow('03', image3)
cv2.imshow('04', image4)

print("WAITING KEY INPUT")
cv2.waitKey(0)

cv2.destroyAllWindows()
print("DESTORY ALL WINDOWS")



'''
테스트용 
# '''
# image1_xy = [[537, 292], [347, 302], [112, 151]]
# # 상단 왼쪽
# image2_xy = [[60, 283], [245, 305], [530, 162]]
# # 상단 오른쪽
# image3_xy = [[542, 39], [537, 155], [354, 55]]
# # 하단 왼쪽
# image4_xy = [[63, 30], [56, 147], [247, 52]]
# # 하단 오른쪽

image1_xy = [[1785, 967], [1054, 943], [856, 823]]
image2_xy = [[190, 939], [809, 1012], [1173, 843]]
image3_xy = [[1806, 138], [1599, 422], [1073, 145]]
image4_xy = [[204, 106], [343, 400], [945, 135]]


image13_angle = get_angle(image1_xy) - get_angle(image3_xy)
image24_angle = get_angle(image2_xy) - get_angle(image4_xy)
rotatem13 = cv2.getRotationMatrix2D((image3_xy[0][0], image3_xy[0][1]), image13_angle, 1)
# rotatem13 = cv2.getRotationMatrix2D((image3_xy[0][0], image3_xy[0][1]), 0, 1)

rotatem24 = cv2.getRotationMatrix2D((image4_xy[0][0], image4_xy[0][1]), image24_angle, 1)
# rotatem24 = cv2.getRotationMatrix2D((image4_xy[0][0], image4_xy[0][1]), 0, 1)


# 연산 START
start = cv2.getTickCount()

#1, 3번 화면
# image1 = cv2.imread(path_01, cv2.IMREAD_COLOR)
# image1_resize = cv2.resize(image1, dsize=(0,0), fx=1, fy=1, interpolation=cv2.INTER_AREA)
#
# image3 = cv2.imread(path_03, cv2.IMREAD_COLOR)
# image3_resize = cv2.resize(image3, dsize=(0,0), fx=1, fy=1, interpolation=cv2.INTER_AREA)

im3h, im3w, im3c =image3_resize.shape

# print(rotatem)
image3_rotate = cv2.warpAffine(image3_resize, rotatem13, (im3w, im3h))



image1_crop = image1_resize[:image1_xy[0][1], :] # 1번 아래쪽 컷
image3_crop = image3_rotate[image3_xy[0][1]:, :] # 3번 위쪽 컷
image13_crop = cv2.vconcat([image1_crop, image3_crop])[image1_xy[0][1] - screen_height : image1_xy[0][1] + screen_height ,image1_xy[0][0]-screen_width:image1_xy[0][0]] # 1,3 concat 오른쪽 컷

#2, 4번 화면
#
# image2 = cv2.imread(path_02, cv2.IMREAD_COLOR)
# image2_resize = cv2.resize(image2, dsize=(0,0), fx=1, fy=1, interpolation=cv2.INTER_AREA)
#
# image4 = cv2.imread(path_04, cv2.IMREAD_COLOR)
# image4_resize = cv2.resize(image4, dsize=(0,0), fx=1, fy=1, interpolation=cv2.INTER_AREA)

im4h, im4w, im4c =image3_resize.shape
image4_rotate = cv2.warpAffine(image4_resize, rotatem24, (im4w, im4h))

image2_crop = image2_resize[:image2_xy[0][1], :] # 2번 아래쪽 컷
image4_crop = image4_rotate[image4_xy[0][1]:, :] # 4번 위쪽 컷
image24_crop = cv2.vconcat([image2_crop, image4_crop])[image2_xy[0][1]-screen_height:image2_xy[0][1]+screen_height,image2_xy[0][0]:image2_xy[0][0] + screen_width] # 2,4 concat 왼쪽 컷
# image2_xy = [[58, 282], [245, 305], [530, 162]]


total = cv2.hconcat([image13_crop, image24_crop])

end = cv2.getTickCount()

# cv2.imshow('01', image1_resize)
# cv2.imshow('03', image3_crop)
cv2.imshow("13", image13_crop)
cv2.imshow("24", image24_crop)
cv2.imshow("total", total)
print("time : {}".format((end-start)/cv2.getTickFrequency()))

print("WAITING KEY INPUT")
cv2.waitKey(0)

cv2.destroyAllWindows()
print("DESTORY ALL WINDOWS")

print("image1_xy = {}".format(image1_xy))
print("image2_xy = {}".format(image2_xy))
print("image3_xy = {}".format(image3_xy))
print("image4_xy = {}".format(image4_xy))

# cv2.imshow('concat', total)




