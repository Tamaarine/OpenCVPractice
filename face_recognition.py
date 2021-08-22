import numpy as np
import cv2 as cv 
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

people = ['ahri']

# Testing the validation
img = cv.imread(os.path.join(os.getcwd(), "league_val", "ahri", "6.jpg"))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Unknown Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    face_roi = gray[y: y+h, x: x+w]
    
    # Make a prediction on this region of interest, the detected face
    label, confidence = face_recognizer.predict(face_roi)
    
    print(f'Label = {people[label]} with a confidence level of {confidence}')
    
    cv.putText(img, f"This is {people[label]}", (0, 0), cv.FONT_HERSHEY_SIMPLEX, 5, (0, 255,0), thickness=2)
    
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
    
cv.imshow('Detected Face', img)

cv.waitKey(0)
