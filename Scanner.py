import cv2
import mediapipe as mp

# Initialize MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.5)

# Define finger tip landmarks
FINGER_TIPS = [4, 8, 12, 16, 20]

def count_fingers(hand_landmarks, frame_width, frame_height):
    finger_count = 0
    landmarks = hand_landmarks.landmark

    # Convert landmarks to pixel coordinates
    landmark_coords = [(int(lm.x * frame_width), int(lm.y * frame_height)) for lm in landmarks]

    # Thumb (check horizontal direction based on hand orientation)
    if landmark_coords[4][0] > landmark_coords[3][0]:
        finger_count += 1

    # Other four fingers (tip higher than lower joint)
    for tip_id in FINGER_TIPS[1:]:
        if landmark_coords[tip_id][1] < landmark_coords[tip_id - 2][1]:
            finger_count += 1

    return finger_count

def process_frame(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    five_fingers_detected = False

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count fingers
            h, w, _ = frame.shape
            finger_count = count_fingers(hand_landmarks, w, h)

            
            # Trigger detection flag
            if finger_count == 5:
                five_fingers_detected = True

    return frame, five_fingers_detected
