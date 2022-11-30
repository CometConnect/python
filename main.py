import cv2
import mediapipe as mp

utils = mp.solutions.drawing_utils
styles = mp.solutions.drawing_styles
hands = mp.solutions.hands

tops = [4, 8, 12, 16, 20]
bottoms = [2, 6, 10, 14, 18]

vid = cv2.VideoCapture(0)

with hands.Hands(
        model_complexity=0,
        min_tracking_confidence=0.5,
        min_detection_confidence=0.5
) as hands:
    while vid.isOpened():
        _, frame = vid.read()
        fingers = 0

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
        for i in range(5):
            top = tops[i]
            bottom = bottoms[i]

            toplm = hlms[top]
            bottomlm = hlms[bottom]

            if toplm.y < bottomlm.y: # the y - axis of flipped
                fingers += 1

        for hlm in raw:
            utils.draw_landmarks(frame, hlm, None, styles.get_default_hand_landmarks_style(),
                                 styles.get_default_hand_connections_style())

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        frame = cv2.flip(frame, 1)
        cv2.putText(frame, f"Fingers: {fingers-1}", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.imshow("Image", frame)
        cv2.waitKey(5)
