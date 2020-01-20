import cv2
import numpy as np

thresh = 85
max_val =255

thresholdType = cv2.THRESH_BINARY

img = cv2.imread("img.bmp",0).astype( 'float32' ) 
median = cv2.medianBlur(img,5)

star =img - median
cv2.imwrite("star.bmp",star)
ret,star = cv2.threshold(star,thresh,max_val,thresholdType)
cv2.imwrite("star_binari.bmp",star)
