import cv2

image = "FaceDetection/4f.jpg"

data = cv2.imread(image)
formatted = cv2.cvtColor(data, cv2.COLOR_RGB2GRAY)


classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = classifier.detectMultiScale(formatted)

output = []
for [x, y, width, height] in faces:
    faceImage = data[y:y+height, x:x+width]
    name = str(x + y + width + height) + ".png"
    cv2.imwrite(name, faceImage)