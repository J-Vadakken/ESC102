import cv2 as cv
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe.python.solutions.drawing_styles as drawing_styles


hands = mp_hands.Hands(
    static_image_mode = False,
    max_num_hands = 2,
    min_detection_confidence = 0.5)

cam = cv.VideoCapture(0)

upper_line_y = 100  # Change this value as needed
lower_line_y = 400  # Change this value as needed

while cam.isOpened():
    success, frame = cam.read()

    cv.line(frame, (0, upper_line_y), (frame.shape[1], upper_line_y), (0, 255, 0), 2)
    cv.line(frame, (0, lower_line_y), (frame.shape[1], lower_line_y), (0, 255, 0), 2)

    # Ensure warning for not success
    if not success:
        print("Couldn't access the camera")
        continue

    # Convert the BGR image to RGB
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    hands_detected = hands.process(frame)

    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)


    # Define the landmark names
    landmark_names = {
        0: "WRIST",
        1: "THUMB_CMC",
        2: "THUMB_MCP",
        3: "THUMB_IP",
        4: "THUMB_TIP",
        5: "INDEX_FINGER_MCP",
        6: "INDEX_FINGER_PIP",
        7: "INDEX_FINGER_DIP",
        8: "INDEX_FINGER_TIP",
        9: "MIDDLE_FINGER_MCP",
        10: "MIDDLE_FINGER_PIP",
        11: "MIDDLE_FINGER_DIP",
        12: "MIDDLE_FINGER_TIP",
        13: "RING_FINGER_MCP",
        14: "RING_FINGER_PIP",
        15: "RING_FINGER_DIP",
        16: "RING_FINGER_TIP",
        17: "PINKY_MCP",
        18: "PINKY_PIP",
        19: "PINKY_DIP",
        20: "PINKY_TIP"
    }

    if hands_detected.multi_hand_landmarks:
        for hand_landmarks in hands_detected.multi_hand_landmarks:
            hand_data = []
            for id, landmark in enumerate(hand_landmarks.landmark):
                hand_data.append([landmark.x, landmark.y, landmark.z])

                landmark_y_pixel = int(landmark.y * frame.shape[0])  # Convert to pixel value
                if landmark_y_pixel < upper_line_y:
                    print(f'{landmark_names[id]} is too high')
                elif landmark_y_pixel > lower_line_y:
                    print(f'{landmark_names[id]} is too low')

            drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style()
            )

        # open the camera
        cv.imshow("Show Video", frame)

        # enable quit
        if cv.waitKey(20) & 0xff == ord('q'):
            break

cam.release()

