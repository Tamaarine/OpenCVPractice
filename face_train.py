import os
import cv2 as cv
import numpy as np

# Using opencv's built in face recognizer
# train the recognizer on those images we have 
people = []

for folder in os.listdir(os.path.join(os.getcwd(), 'league')):
    people.append(folder)
print(people)

# Loop over every folder, and loop over every image
# and grab the face then add it to the training set
feature = [] # The image array of the faces
labels = [] # Whose face does the image belong to, pair with feature. It is the index it is mapped

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(os.getcwd(), "league", person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            # Read the image
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x, y, w, h) in face_rect:
                face_roi = gray[y: y+h, x:x+w]
                feature.append(face_roi)
                labels.append(label)
                
# Basically after the function, feature stores the coordinate
# of the face detected in each one. Then the corresponding 
# element in labels stores the index into people in which it tells
# the name of the face in the people array
create_train()

# Instanitated face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Convert to numpy array
feature = np.array(feature, dtype='object')
labels = np.array(labels)

# Train the recognizer on the feature list and label
face_recognizer.train(feature, labels)  

print("Training done")

# Save the feature and labels np array
# np.save('feature.npy', feature)
# np.save('labels.npy', labels)


# Instead of training all over again
# we can save this trained model to a place and then just load the model
# Save it as a yml file
face_recognizer.save('face_trained.yml')
            
            
            
            
            
            
            
            