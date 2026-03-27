import math
def calculate_angle(a, b, c):
    
    ab = [a.x - b.x, a.y - b.y]
    cb = [c.x - b.x, c.y - b.y]
    
    dot = ab[0] * cb[0] + ab[1] * cb[1]
    mag_ab = math.sqrt(ab[0]**2 + ab[1]**2)
    mag_cb = math.sqrt(cb[0]**2 + cb[1]**2)
    
    if mag_ab * mag_cb == 0:
        return 0.0
    
    angle = math.acos(dot / (mag_ab * mag_cb))
    return math.degrees(angle)

def get_finger_angles(landmarks):
    angles = []
    
    angles.append(calculate_angle(landmarks[2], landmarks[3], landmarks[4]))  # Thumb
    
    finger_joints = [ (5, 6, 8), # Index
                     (9, 10, 12), # Middle
                     (13, 14, 16), # Ring
                     (17, 18, 20) # Pinky
    ]
    
    for base, mid, tip in finger_joints:
        angle = calculate_angle(landmarks[base],
                                landmarks[mid],
                                landmarks[tip]
        )
        angles.append(angle)
    return angles