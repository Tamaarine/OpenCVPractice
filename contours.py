import cv2 as cv 
import numpy as np

img = cv.imread('img/cat.jpg')

cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# How to identify contours. Contours are boundary of object. Useful for object detection
# Edge and contours are not the same thing mathematically 

# Convert the image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# # Do a blur before finding contours
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Grab the edges
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)


# Threshhold basically binarize the matrix, 0 or 255 for each pixel
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)



# Grab the contours
# Looks at the edge found, and return contours
# The variable contours -> Python list of all the coordinates of all the contours found in the image
# hierarchies -> Refers to the hierarchical representation of the contours (out of the scope for beginner)
# RETR_LIST return all contours, RETR_EXTERNAL return contours outside
# CHAIN_APPROX_NONE -> how we approximate contours, NONE doesn't approximate, just return all contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))

# Use canny to find contours and draw them


# Draw contour
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)