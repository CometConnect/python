import cv2

classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')
cap = cv2.VideoCapture('walking.avi')

while True:
    ret, frame = cap.read()

    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    except:
        break  # this happens when the video ends
    faces = classifier.detectMultiScale(gray)

    for [x, y, width, height] in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)

    cv2.imshow("Image", frame)
    if cv2.waitKey(1) == 32:  # Space
        break

cap.release()
cv2.destroyAllWindows()
