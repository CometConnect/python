import cv2
import numpy
from keras.models import Sequential
from enum import Enum

vid = cv2.VideoCapture(0)
model = Sequential()


class Gesture(Enum):
    Scissors = 0
    Paper = 1
    Rock = 2


def get_gesture(image) -> tuple[Gesture, float]:
    resized = numpy.resize(image, (len(image[0]), len(image)))
    normalized = resized/numpy.linalg.norm(resized, 1)

    predictions = model.predict(normalized)
    print(predictions[0][0], " Scissors")
    print(predictions[0][1], " Paper")
    print(predictions[0][2], " Rock")

    return Gesture(0), float(predictions[0][0])


while True:
    status, frame = vid.read()
    if status:
        frame = cv2.flip(frame, 1)
        gesture, score = get_gesture(frame)

        cv2.putText(frame, f"{gesture.name}: {score}%", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        cv2.imshow('Cam', frame)
        if cv2.waitKey(1) == 32:
            break
    else:
        break

vid.release()
