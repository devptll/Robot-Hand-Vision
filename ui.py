import cv2

def draw_ui(frame, angles):
    labels = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
    
    cv2.rectangle(frame, (0, 0), (400, 280), (30, 30, 30), -1)
    
    for i, (label, angle) in enumerate(zip(labels, angles)):
        y = 50 + i * 40
        
        text = f"{label}: {int(angle)} deg"
        cv2.putText(frame, text, (10, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        bar_x = 180
        bar_width = int((angle / 180) * 180)
        
        cv2.rectangle(frame,
                        (bar_x, y - 15), 
                        (bar_x + bar_width, y), 
                        (0, 255, 0), -1)
        
    return frame