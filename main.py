import cv2
from hand_tracker import HandTracker
from utils import get_finger_angles
from ui import draw_ui

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = tracker.find_hands(frame)
        
        if results.hand_landmarks:
            for handLms in results.hand_landmarks:
                angles = get_finger_angles(handLms)
                frame = draw_ui(frame, angles)

        cv2.imshow("Robotics Hand UI", frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()