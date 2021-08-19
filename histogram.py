import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('img/cat.jpg')
cv.imshow('Cat', img)

# Histogram allow you to visual the distribution of pixel
# intensity in an image whether is grayscale or a BGR image

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank.copy(), (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image', masked)

# Need to pass in a list of image, and the number of channels
# gray_hist = cv.calcHist([gray], [0], masked, [256], [0, 256])

# Color histogram
plt.figure()
plt.title('Grayscale historgram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)

