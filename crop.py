import cv2

def facechop(image):  
    facedata = "trained_classifier.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

        sub_face = img[y:y+h, x:x+w]
        face_file_name = "faces/face_" + str(y) + ".jpg"
        resized_image = cv2.resize(sub_face, (100, 100)) 
        cv2.imshow(face_file_name, resized_image)

   
    return

if __name__ =='__main__':  
    facechop("img3.jpg")

    while(True):
        key = cv2.waitKey(20)
       