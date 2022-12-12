import numpy as np
import pyautogui
import imutils
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

delay = 20
last_click = 0
clicks = 0

finger_tips = [8, 12, 16, 20]
thumb_tip = 4

while True:
    last_click += 1
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            # accessing the landmarks by their position
            lm_list = []
            for _, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

            # array to hold true or false if finger is folded
            finger_fold_status = []
            for tip in finger_tips:
                x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)
                if lm_list[tip].x < lm_list[tip - 3].x:
                    cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)
            if all(finger_fold_status) and delay < last_click:
                print("Clicking")
                clicks += 1
                last_click = 0
                image = pyautogui.screenshot()
                image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                cv2.imwrite(f"screenshots/{clicks}.png", image)
                # WRITE THE CODE HERE
            mp_draw.draw_landmarks(img, hand_landmark,
                                   mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0, 0, 255), 2, 2),
                                   mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                   )

    cv2.imshow("hand tracking", img)
    if cv2.waitKey(1) == 32:
        break
