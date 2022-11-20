import cv2
import os

images = os.listdir("Images")
length = len(images)

i = 0

while True:
    data = cv2.imread(f"Images/{images[i]}")

    cv2.imshow("Album", data)

    cv2.waitKey(2000)
    i += 1

    if i == length:
        break