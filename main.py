import cv2

img = cv2.imread("solar-system.jpg")


def makeText(text: str, position: tuple):
    cv2.putText(img, text, position, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))


mappings = [
    ["Sun", (20, 300)],
    ["Mercury", (100, 200)],
    ["Venus", (190, 170)],
    ["Earth", (290, 260)],
    ["Mars", (380, 260)],
    ["Jupiter", (500, 70)],
    ["Saturn", (800, 150)],
    ["Uranus", (950, 150)],
    ["Neptune", (1100, 150)]
]

for mapping in mappings:
    makeText(mapping[0], mapping[1])

cv2.imwrite("solar-system-with-names.jpg", img)