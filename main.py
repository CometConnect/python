import numpy
import cv2

data = numpy.zeros((600, 600))


def sqr(i):
    return i * i


for i in range(len(data) - 1):
    for j in range(len(data[i]) - 1):
        if sqr(i - 300) + sqr(j - 300) <= sqr(200):
            data[i][j] = 255

cv2.imshow("Circle", data)
cv2.waitKey(0)
