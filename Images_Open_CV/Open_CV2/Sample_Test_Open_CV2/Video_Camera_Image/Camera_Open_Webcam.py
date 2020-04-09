import cv2

cap = cv2.VideoCapture(0)  # open the camera

while True:
    ret, frame = cap.read()  # read the camera stream
    # ret : hold the value, frame : access the camera with help of frame
    cv2.imshow("Live Video Camera ", frame)  # show camera / video
    if cv2.waitKey(1) == 13:  # asking code = 13 : close the camera
        break

cap.release()
cv2.destroyAllWindows()
