#ASCII Real-Time Video Feed
import cv2

chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (100, 40))
    
    ascii_frame = ""
    for row in resized:
        for pixel in row:
            ascii_frame += chars[pixel // 25]
        ascii_frame += "\n"
    
    print("\033[H" + ascii_frame) # Clears terminal and prints
    if cv2.waitKey(1) & 0xFF == ord('q'): break