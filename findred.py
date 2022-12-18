import cv2
import numpy as np

ball_color = 'red'
color_range = {'red': {'Lower': np.array([0, 50, 10]), 'Upper': np.array([11, 255, 255])}}
img = cv2.imread('redball.png')   #输入要读取的图像

# 先对图像进行一个高斯模糊
gs_img = cv2.GaussianBlur(img, (5, 5), 0)

# 将原来BGR格式的图像转换成HSV格式
hsv = cv2.cvtColor(gs_img, cv2.COLOR_BGR2HSV)

# 对图像进行一个腐蚀的操作
erode_hsv = cv2.erode(hsv, None, iterations=2)
inRange_hsv = cv2.inRange(erode_hsv, color_range[ball_color]['Lower'], color_range[ball_color]['Upper'])
cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

c = max(cnts, key=cv2.contourArea)
rect = cv2.minAreaRect(c)
box = cv2.boxPoints(rect)
point = str(box[0][0]) + ', ' + str(box[0][1])

#描边和输出坐标
cv2.drawContours(img, [np.int0(box)], -1, (0, 0, 255), 2)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, point, (140,410),font, 0.5, (0, 0, 255),2)

#展示结果
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()