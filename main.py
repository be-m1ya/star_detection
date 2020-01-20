import cv2
import numpy as np

#画像により調整
thresh = 85
max_val =255
thresholdType = cv2.THRESH_BINARY

#floatで画像をロード
img = cv2.imread("img.bmp",0).astype( 'float32' ) 
median = cv2.medianBlur(img,5)

star = img - median
ret,star = cv2.threshold(star,thresh,max_val,thresholdType)
cv2.imwrite("star.bmp",star)
