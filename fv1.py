import cv2
import numpy as np
from retinaface import RetinaFace
import matplotlib.pyplot as plt
import mss
import time

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # اختر الشاشة الأولى
        while True:
            sct_img = sct.grab(monitor)
            img = np.array(sct_img)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            yield img

def process_image(image):
    faces = RetinaFace.detect_faces(image)
    for key, face in faces.items():
        facial_area = face['facial_area']
        color = (0, 255, 0) if 'embedding' in face else (0, 0, 255)
        cv2.rectangle(image, (facial_area[0], facial_area[1]), (facial_area[2], facial_area[3]), color, 2)
    
    return image

def main():
    print("Recording screen and processing...")
    screen_capture = capture_screen()

    for img in screen_capture:
        processed_image = process_image(img)
        cv2.imshow("Screen", processed_image)
        
        # اضغط على 'q' للخروج من العرض
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()