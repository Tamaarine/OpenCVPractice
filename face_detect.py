import cv2 as cv

img = cv.imread('img/lady4.jpg')
cv.imshow('Lady 1', img)

# Face recognition doesn't care about skin tones
# it uses grayscale edges to try to detect faces

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

# Now next we read in the harr_face.xml file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# And we detect faces next
# return the rectangular coordiantes on the detected face
# less minNeighbors value are more prone to noises
# greater minNeighbors value are more strict on detecting faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(len(faces_rect))

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow('Detected faces', img)

# Haar cascade is very sensitive to noises
# and it will detect faces that aren't faces
# Better face recongition classifiers available


cv.waitKey(0)

