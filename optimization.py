'''
최대한 최적화 코드
목표 시간 : 0.14 -> 0.03
'''

__author__= "yunghn3@gmail.com"

import cv2
import numpy
import matplotlib
import math
import time

cv2.setUseOptimized(True)
print(cv2.useOptimized())

path_01 = "/Users/yungeontaeg/myworkspace/COMARTSYSTEM/Panorama/PanoramaProject/resource/01_new.jpg"
path_02 = "/Users/yungeontaeg/myworkspace/COMARTSYSTEM/Panorama/PanoramaProject/resource/02_new.jpg"
path_03 = "/Users/yungeontaeg/myworkspace/COMARTSYSTEM/Panorama/PanoramaProject/resource/03_new.jpg"
path_04 = "/Users/yungeontaeg/myworkspace/COMARTSYSTEM/Panorama/PanoramaProject/resource/04_new.jpg"

screen_width = int(250 * (10 / 3))
screen_height = int(150 * (10 / 3))

def get_angle(arr):
    return math.degrees(math.atan2(arr[1][0]-arr[2][0], arr[1][1]-arr[2][1]))

def get_angle2(arr):
    return math.degrees(math.atan2(arr[1][1]-arr[2][1], arr[2][0]-arr[1][0]))

image1_xy = [[537, 292], [347, 302], [112, 151]]
# 상단 왼쪽
image2_xy = [[60, 283], [245, 305], [530, 162]]
# 상단 오른쪽
image3_xy = [[542, 39], [537, 155], [354, 55]]
# 하단 왼쪽
image4_xy = [[63, 30], [56, 147], [247, 52]]
# 하단 오른쪽

for i in range(len(image1_xy)):
    image1_xy[i][0] = int(float(image1_xy[i][0]) * 3.33)
    image1_xy[i][1] = int(float(image1_xy[i][1]) * 3.33)

for i in range(len(image2_xy)):
    image2_xy[i][0] = int(float(image2_xy[i][0]) * 3.33)
    image2_xy[i][1] = int(float(image2_xy[i][1]) * 3.33)

for i in range(len(image3_xy)):
    image3_xy[i][0] = int(float(image3_xy[i][0]) * 3.33)
    image3_xy[i][1] = int(float(image3_xy[i][1]) * 3.33)

for i in range(len(image4_xy)):
    image4_xy[i][0] = int(float(image4_xy[i][0]) * 3.33)
    image4_xy[i][1] = int(float(image4_xy[i][1]) * 3.33)

image13_angle = get_angle(image1_xy) - get_angle(image3_xy)
image24_angle = get_angle(image2_xy) - get_angle(image4_xy)

rotatem13 = cv2.getRotationMatrix2D((image3_xy[0][0], image3_xy[0][1]), image13_angle, 1)
# rotatem13 = cv2.getRotationMatrix2D((image3_xy[0][0], image3_xy[0][1]), 0, 1)
rotatem24 = cv2.getRotationMatrix2D((image4_xy[0][0], image4_xy[0][1]), image24_angle, 1)
# rotatem24 = cv2.getRotationMatrix2D((image4_xy[0][0], image4_xy[0][1]), 0, 1)


# 연산 START
start = cv2.getTickCount()

#1, 3번 화면
image1 = cv2.imread(path_01, cv2.IMREAD_COLOR)

image3 = cv2.imread(path_03, cv2.IMREAD_COLOR)

im3h, im3w, im3c =image3.shape

# print(rotatem)

image3_rotate = cv2.warpAffine(image3, rotatem13, (im3w, im3h))



image1_crop = image1[:image1_xy[0][1], :] # 1번 아래쪽 컷
image3_crop = image3_rotate[image3_xy[0][1]:, :] # 3번 위쪽 컷
image13_crop = cv2.vconcat([image1_crop, image3_crop])[image1_xy[0][1] - screen_height : image1_xy[0][1] + screen_height ,image1_xy[0][0]-screen_width:image1_xy[0][0]] # 1,3 concat 오른쪽 컷

#2, 4번 화면

image2 = cv2.imread(path_02, cv2.IMREAD_COLOR)

image4 = cv2.imread(path_04, cv2.IMREAD_COLOR)

im4h, im4w, im4c =image3.shape
image4_rotate = cv2.warpAffine(image4, rotatem24, (im4w, im4h))

image2_crop = image2[:image2_xy[0][1], :] # 2번 아래쪽 컷
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