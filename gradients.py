import cv2 as cv
import numpy as np

img = cv.imread('img/cat.jpg')
cv.imshow('Cat', img)

# Canny edge detection is one way of detecting
# edges, another way is laplacian and sobel

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Canny 
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny', canny)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)

# Convert all negative value to positive
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel compute gradient in two directions
# x axis and y axis
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)

# We can combine those two edge
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined sobel', combined_sobel)

# Canny edge detection is more advance and cleaner
# but sobel is used in advancer topics

cv.waitKey(0)