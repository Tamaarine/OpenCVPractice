# Masking allow us to focus on certain part of the image
import cv2 as cv
import numpy as np

img = cv.imread('img/cat.jpg')
cv.imshow('cat', img)

# dimension of mask must be the same as the image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank.copy(), (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow('Mask', mask)

# We want to mask the image over the cat image
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked cat', masked)

# Rect mask
rect_mask = cv.rectangle(blank.copy(), (0, 0), (200, 200), 255, -1)
cv.imshow('Rect mask', rect_mask)

masked_rect = cv.bitwise_and(img, img, mask=rect_mask)
cv.imshow('Rect masked', masked_rect)


cv.waitKey(0)