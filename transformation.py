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
translated = translate(img, -100, 200)
cv.imshow('Translated', translated)

translated = translate(img, 100, -200)
cv.imshow('Translated2', translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    # rotate around cneter
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)
    
rotated = rotate(img, 90)
cv.imshow('Rotated', rotated)


# Flipped image, 1 or -1 or 0.
# 0 = flip vertically
# 1 = flip horizontally
# -1 = flip both vertically and horizontally
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)


# cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)