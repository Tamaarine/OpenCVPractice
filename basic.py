import cv2 as cv

img = cv.imread('img/cat.jpg')

cv.imshow('Cat', img)

# Convert to greyscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)


# Dilating the image. Basically highlighting making the edges thicker
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)


# Eroding, basically it dim the edges, opposite of dilated
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)


# Resize, interpolation means to estimate the value in between that isn't determined
resized = cv.resize(img, (100, 100), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)


# Cropping
cropped = img[50: 200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)