import cv2

# img = cv2.imread('img/cat.jpg')

# cv2.imshow('Cat', img)

# Reading video
capture = cv2.VideoCapture(0)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)
    
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    
    cv2.imshow('Video', frame)
    cv2.imshow('Video Resized', frame_resized)
    
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()