import cv2
import numpy as np
import pyautogui


def gesture_controls():

    cap = cv2.VideoCapture(0)
    # red_lower = np.array([155,25,0])
    # red_upper = np.array([179,255,255])
    #
    # yello_lower = np.array([22, 93, 0])
    # yello_upper = np.array([45, 255, 255])
    blue_lower=np.array([100,150,0],np.uint8)
    blue_upper=np.array([140,255,255],np.uint8)
    prev_y = 0
    while True:
        ret, frame = cap.read()
        geay = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(geay, blue_lower, blue_upper)
        contours, heirarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            area = cv2.contourArea(c)
            if area > 700:
                x,y,w,h = cv2.boundingRect(c)
                # cv2.drawContours(frame, c, -1, (0, 255, 0), 2)
                cv2.rectangle(frame, (x,y) , (x+w, y+h), (0, 255, 0), 2)
                if prev_y-y > 50:
                    print('moving down')
                    pyautogui.press('space')
                prev_y = y

        cv2.imshow('Social Media',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()



