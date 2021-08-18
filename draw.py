import cv2 as cv
import numpy as np

# img = cv.imread('img/cat.jpg')
# cv.imshow('Cat', img)

# Make a blank matrix that is all black
# and display it
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Point the image a certain color
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)

# Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1)
cv.imshow('Green', blank)

# Draw a circle
cv.circle(blank, (250, 250), 40, (255,0,0), thickness=-1)
cv.imshow('Green', blank)

# Draw a line
cv.line(blank, (0, 0), (250, 250), (0, 0, 255), thickness=3)
cv.imshow('Green', blank)

# Write a text
cv.putText(blank, 'Hello my name is Ricky', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 255), 2)
cv.imshow('Green', blank)





cv.waitKey(0)