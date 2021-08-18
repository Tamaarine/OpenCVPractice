import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread('img/cat.jpg')
cv.imshow('Cat', img)

# Color space are space of color, a system to represent
# pixel of colors. RGB, HSV, LAB are all color spaces
# and we can convert between different color spaces

# BGR is the default opencv color space and we can convert it to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (hue saturation value) based on how human think about colors
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# Matplotlib uses RGB colorspace so we see an inversion of color spaces
# plt.imshow(img)
# plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# # Now opencv will show the inversion colorspace
# plt.imshow(rgb)
# plt.show()

# You cannot convert grayscale to HSV directly
# Have to convert to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

# Then convert BGR to grayscale



cv.waitKey(0)