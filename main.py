import cv2
import mediapipe as mp
from pynput.keyboard import Controller, Key

utils = mp.solutions.drawing_utils
styles = mp.solutions.drawing_styles
hands = mp.solutions.hands

tops = [4, 8, 12, 16, 20]
bottoms = [2, 6, 10, 14, 18]

vid = cv2.VideoCapture(0)
controller = Controller()
prev = 0

with hands.Hands(
        model_complexity=0,
        min_tracking_confidence=0.5,
        min_detection_confidence=0.5
) as hands:
    while vid.isOpened():
        _, frame = vid.read()
        fingers = 0
        direction = "null"

        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame)
        raw = results.multi_hand_landmarks
        if not raw:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame = cv2.flip(frame, 1)
            cv2.imshow("Image", frame)
            cv2.waitKey(5)
            continue

        hlms = raw[0].landmark
        if hlms[0].x < hlms[8].x:
            direction = "right"
        else:
            direction = "left"
        for i in range(5):
            top = tops[i]
            bottom = bottoms[i]

            toplm = hlms[top]
            bottomlm = hlms[bottom]

            if not i == 0:
                if toplm.y < bottomlm.y:
                    fingers += 1
        for hlm in raw:
            utils.draw_landmarks(frame, hlm, None, styles.get_default_hand_landmarks_style(),
                                 styles.get_default_hand_connections_style())

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.flip(frame, 1)

        if fingers == 0 and not prev == 0:
            controller.press(Key.space)
        elif fingers == 1 and direction == "left":
            controller.press(Key.right)  # THE FRAME IS FLIPPED WHILE CHECKING
        elif fingers == 1 and direction == "right":
            controller.press(Key.left)

        cv2.waitKey(5)
        prev = fingers
