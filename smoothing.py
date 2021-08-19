import cv2 as cv

img = cv.imread('img/cat.jpg')
cv.imshow('cat', img)

# Kernel is a specific window over a image and the size of the kernel is called the kernel size
# Blur is applied to the middle pixel 

# There are different method of blurring

# 1. Average, the middle pixel is computed as the average of the surrounding pixel intensity
average = cv.blur(img, (7,7))
cv.imshow('Average blur', average)

# The higher the kernel size, the more blur


# 2. Gaussian blur, same averaging method with but each pixel has a weight associated to it
#  More natural blur compare to method one. The third argument is the standard deviation
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gasussian blur', gauss)

# 3. Median blur, same as averaging but instead of finding average, you find the median of the surrounding
# pixel. It is generally more effective in removing noises, in removing them
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# 4. Bilateral blur. The most effective, apply blur but retain the edges
# sigmaColor, more color consider neighbor
# sigmaSpace, more sigmaSpace determine how further away pixels affect the blurring for the center pixel
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)