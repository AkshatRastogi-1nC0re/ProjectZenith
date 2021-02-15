from imutils.video import VideoStream
import tensorflow.keras
import numpy as np
import cv2
from process_labels import gen_labels
import winsound


def recognize_mask():
    try:
        face_cascade = cv2.CascadeClassifier('converted_keras\\haarcascade_frontalface_alt2.xml')
        np.set_printoptions(suppress=True)
        #image = cv2.VideoCapture(0)
        vs = VideoStream(src=0).start()

        model = tensorflow.keras.models.load_model('converted_keras\\keras_model.h5')

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # A dict that stores the labels
        labels = gen_labels()
        font = cv2.FONT_HERSHEY_SIMPLEX

        listA = []

        n = 1
        while n<=30:
            img = vs.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
                frame2 = cv2.resize(img, (224, 224)) # turn the image into a numpy array
                image_array = np.asarray(frame2) # Normalize the image
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1  # Load the image into the array
                data[0] = normalized_image_array
                pred = model.predict(data)
                result = np.argmax(pred[0])

                cv2.putText(faces, "Label : " +
                            labels[str(result)], (280, 400), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
                listA.append(labels[str(result)])# winsound.Beep(2500,1000)
                n += 1

            # cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break

        vs.stop()
        m = 0
        wm = 0
        for i in listA:
            if i == "with_mask":
                m += 1
            else:
                wm += 1
        if m>wm:
            return("Mask Detected")
        else:
            return("Mask not Detected")
    except:
        return ("Face Not Detected")
