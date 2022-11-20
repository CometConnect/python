import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    formatted = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    faces = classifier.detectMultiScale(formatted)
    for [x, y, width, height] in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 0), 2)

    cv2.imshow("Web cam", frame)

    if cv2.waitKey(25) == 32:
        break

vid.release()
cv2.destoryAllWindows()