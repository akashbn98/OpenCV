import cv2

face_cascade = cv2.CascadeClassifier('trained_classifier.xml')
# Read the input image
img = cv2.imread('img3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y , w ,h) in faces:
     cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
 