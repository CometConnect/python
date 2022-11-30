import math

import cv2

vid = cv2.VideoCapture('bb3.mp4')
tracker = cv2.TrackerCSRT_create()

_, frame = vid.read()
tracker.init(frame, cv2.selectROI("Image", frame))


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)


def sqaure(x):
    return x * x


def find_center(x, y, width, height):
    return x + width / 2, y + height / 2


target = find_center(478, 254, 85, 80)


def distance_from_target(x, y):
    # √(x₁-x₂)² + (y₁-y₂)²
    return math.sqrt(sqaure(x - target[0]) + sqaure(y - target[1]))


trajectory = [

]


def draw_trajectory(img):
    for pt in trajectory:
        cv2.circle(img, (int(pt[0]), int(pt[1])), 1, (255, 0, 0), 5)


while True:
    _, frame = vid.read()

    _, data = tracker.update(frame)
    drawBox(frame, data)

    center = find_center(data[0], data[1], data[2], data[3])
    trajectory.append(center)

    draw_trajectory(frame)
    cv2.putText(frame, f"Distance from target: {round(distance_from_target(center[0], center[1]))}", (100, 100),
                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

    cv2.imshow("Image", frame)
    cv2.waitKey(1)
