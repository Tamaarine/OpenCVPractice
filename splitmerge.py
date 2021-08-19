import cv2 as cv
import numpy as np

img = cv.imread('img/cat.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# Color image consist of multiple channel, red, green, and blue
# All the image we see are these 3 channel merge together
b, g, r = cv.split(img)

# Merge to make a 3 channel image
# so all the color are getting reporsented in its color
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)
# It shows color channel in gray scale because gray scale only have 1 
# color channel
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)