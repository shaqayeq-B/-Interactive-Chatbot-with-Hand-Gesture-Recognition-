import cv2
import mediapipe as mp
import pyttsx3
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
engine = pyttsx3.init()

# Global variables
last_speech_time = 0
cooldown = 3  # seconds
last_gesture = None
gesture_stable = None
last_gesture_time = 0  # Initialization added

def detect_thumb_position(landmarks):
    thumb_tip = landmarks[4]
    thumb_ip = landmarks[3]
    
    # Correct Y-axis comparison (OpenCV coordinates)
    if thumb_tip.y < thumb_ip.y:  # Thumb DOWN (👎)
        return "👎"
    elif thumb_tip.y > thumb_ip.y:  # Thumb UP (👍)
        return "👍"
    return None

def speak(text):
    global last_speech_time
    current_time = time.time()
    if current_time - last_speech_time > cooldown:
        engine.say(text)
        engine.runAndWait()
        last_speech_time = current_time

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]  # First detected hand
        current_gesture = detect_thumb_position(hand_landmarks.landmark)

        # Stability check (0.5-second delay)
        if current_gesture != last_gesture:
            last_gesture = current_gesture
            gesture_stable = None
        elif time.time() - last_gesture_time > 0.5:
            gesture_stable = current_gesture
            last_gesture_time = time.time()

        # Display and voice feedback
        if gesture_stable == "👍":
            cv2.putText(img, "👍 LIKED", (50, 100), 
                       cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            speak("Great! You liked it. Thank you for the support!")
            
        elif gesture_stable == "👎":
            cv2.putText(img, "👎 DISLIKED", (50, 100), 
                       cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            speak("Noted. You disliked it. We'll improve!")

        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Gesture Detection", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()