from imutils.video import VideoStream
import numpy as np
from deepface import DeepFace


def recogniseMood():
    np.set_printoptions(suppress=True)
    vs = VideoStream(src=0).start()

    listA = []

    n = 1
    while n<=30:
        img = vs.read()
        result = DeepFace.analyze(img, actions=['emotion'])
        listA.append(result['dominant_emotion'])
        n += 2
        if n == 30:
            break

    a = max(set(listA), key=listA.count)
    return a
