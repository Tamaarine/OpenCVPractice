# Convert an image to binary image, each pixel
# is either black (0) or white (255)
# If the pixel is less than the threshold set to 0
# if it is greater than threshold we set it to 255
import cv2 as cv

img = cv.imread('img/cat.jpg')
cv.imshow('Cat', img)

# Convert to a gray scale first
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Two type of thresholding
# simple thresholding
# max is the value you set it to if it is greater than threshold
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
# thresh, the binarized image
# threshold same threshold value you passed in

cv.imshow('Simple threshold image', thresh)


# Inverse of the previous threshold image. Basically reversing the black and white color
threshold, thresh_inv = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold inverse image', thresh_inv)

# Adaptive thresholding, let computer find optimal threshold value
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', adaptive_thresh)




cv.waitKey(0)