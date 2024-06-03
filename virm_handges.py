import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize Mediapipe hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            # Get coordinates of index finger tip and thumb tip
            index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]

            # Convert normalized coordinates to screen coordinates
            index_x, index_y = int(index_finger_tip.x * screen_width), int(index_finger_tip.y * screen_height)
            thumb_x, thumb_y = int(thumb_tip.x * screen_width), int(thumb_tip.y * screen_height)

            # Move the mouse cursor to the position of the index finger tip
            pyautogui.moveTo(index_x, index_y)

            # Detect click gesture (when index finger tip and thumb tip are close)
            distance = np.hypot(index_x - thumb_x, index_y - thumb_y)
            if distance < 50:
                pyautogui.click()

    cv2.imshow("Hand Tracking", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
