import cv2
import mediapipe as mp
from AppOpener import open, close
import pyautogui
import volume_controller as volume
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphand = mp.solutions.hands


cap = cv2.VideoCapture(0)

hands = mphand.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
# print(hands)
def is_thumbs_up(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mphand.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mphand.HandLandmark.THUMB_IP]
    thumb_mcp = hand_landmarks.landmark[mphand.HandLandmark.THUMB_MCP]
    thumb_cmc = hand_landmarks.landmark[mphand.HandLandmark.THUMB_CMC]
    index_tip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_MCP]
    
    
    if (thumb_tip.y < thumb_ip.y < thumb_mcp.y < thumb_cmc.y and
        index_tip.y > index_mcp.y):
        print(thumb_ip, '\n', thumb_ip, '\n', thumb_mcp, '\n', thumb_cmc)
        return True
    return False

def is_thumbs_down(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mphand.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mphand.HandLandmark.THUMB_IP]
    thumb_mcp = hand_landmarks.landmark[mphand.HandLandmark.THUMB_MCP]
    thumb_cmc = hand_landmarks.landmark[mphand.HandLandmark.THUMB_CMC]

    index_tip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_MCP]

    
    # Check if thumb is down and index finger is up
    if (thumb_tip.y > thumb_ip.y > thumb_mcp.y > thumb_cmc.y and
        index_tip.y < index_mcp.y):
        return True
    return False


def is_peace(hand_landmarks):
    index_tip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mphand.HandLandmark.MIDDLE_FINGER_TIP]
    ring_dip = hand_landmarks.landmark[mphand.HandLandmark.RING_FINGER_DIP]
    thumb_tip = hand_landmarks.landmark[mphand.HandLandmark.THUMB_DIP]
    thumb_cmc = hand_landmarks.landmark[mphand.HandLandmark.THUMB_CMC]
    pinky_dip = hand_landmarks.landmark[mphand.HandLandmark.PINKY_DIP]
    
    if True:
        return True

def is_three(hand_landmarks):
    
    index_tip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_TIP]
    index_dip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_DIP]
    pinky_tip = hand_landmarks.landmark[mphand.HandLandmark.PINKY_TIP]
    middle_mcp = hand_landmarks.landmark[mphand.HandLandmark.MIDDLE_FINGER_MCP]
    pinky_dip = hand_landmarks.landmark[mphand.HandLandmark.PINKY_FINGER_DIP]
    
def is_four(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mphand.HandLandmark.THUMB_TIP]
    index_mcp = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_MCP]
    
    

def is_pointing_up(hand_landmarks):
    index_tip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_TIP]
    index_dip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_DIP]
    middle_tip = hand_landmarks.landmark[mphand.HandLandmark.MIDDLE_FINGER_TIP]
    middle_dip = hand_landmarks.landmark[mphand.HandLandmark.MIDDLE_FINGER_DIP]
    wrist = hand_landmarks.landmark[mphand.HandLandmark.WRIST]
    
    # pyautogui.move( int(index_tip.x*20), int(index_tip.y*20))
    
    # print(f'this is indextIP {index_tip.y}')
    # print(f'this is indextDIP {index_dip.y}')
    # print(f'this is middleTIP{middle_tip.y}')
    # print(f'this is middleDIP{middle_dip.y}')
    # print(f'this is Wrist {wrist.y}')
    # print
    # print(index_dip.y > middle_tip.y and index_tip.y > wrist.y)
    # if index_tip.x > middle_tip.x and index_tip.x > wrist.x:
    #     return
    # # if index_tip.x < index_ip.x and :
    # #     return True
    # return False

def is_pointing_down(hand_landmarks):
    index_tip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_TIP]
    index_dip = hand_landmarks.landmark[mphand.HandLandmark.INDEX_FINGER_DIP]
    middle_tip = hand_landmarks.landmark[mphand.HandLandmark.MIDDLE_FINGER_TIP]
    middle_dip = hand_landmarks.landmark[mphand.HandLandmark.MIDDLE_FINGER_DIP]
    wrist = hand_landmarks.landmark[mphand.HandLandmark.WRIST]
    
    if index_dip.y > middle_tip.y and index_tip.y < wrist.y:
        return True
    return False
    # print(f'this is indexDIP {index_ip}')



while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and find hands
    results = hands.process(image)

    # Convert the image color back so it can be displayed
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mphand.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
            is_pointing_up(hand_landmarks)
            
            # if is_pointing_up(hand_landmarks):
            #     cv2.putText(image, 'pointing Up', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            #     open('Netflix')
            # elif is_pointing_down(hand_landmarks):
            #     cv2.putText(image, 'pointing down', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)           
            #     open('spotify')
            # Check if the detected hand shows a thumbs-up gesture
            if is_thumbs_up(hand_landmarks):
                cv2.putText(image, 'Thumbs Up', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                # volume.increase_volume()
                # open('Netflix')
                volume.increase_volume()
            # # Check if the detected hand shows a thumbs-down gesture
            if is_thumbs_down(hand_landmarks):
                cv2.putText(image, 'Thumbs Down', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                volume.decrease_volume()
                # open('spotify')


    # Display the image
    cv2.imshow('Hand Gesture Detection', image)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
