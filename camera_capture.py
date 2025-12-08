#Webcam → Capture Frame → Save JPG
import cv2

def capture_image(filename="capture.jpg"):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imwrite(filename, frame)
    cam.release()
    print("Image Captured")