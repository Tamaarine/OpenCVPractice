import cv2 as cv
import numpy as np

img = cv.imread('img/cat.jpg')

cv.imshow('Cat', img)

# Translation, shift an image up, down, left, or right
# or any combination
def translate(img, x, y):
    # This is the transformation matrix
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
    
# -x = left
# -y = up
# x = right
# y = down
translated = translate(img, 100, 200)
cv.imshow('Translated', translate)