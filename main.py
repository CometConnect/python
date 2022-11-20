import cv2

fps = 50
wait = int(1000 / fps)

vid = cv2.VideoCapture(0)
writer = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (1280, 720), True)

i = 110
while vid.open(f"Images/{i}.jpg"):
    data = vid.read()[1]
    cv2.imshow("Output", data)
    writer.write(data)
    cv2.waitKey(wait)
    i += 1

vid.release()
writer.release()
cv2.destroyAllWindows()