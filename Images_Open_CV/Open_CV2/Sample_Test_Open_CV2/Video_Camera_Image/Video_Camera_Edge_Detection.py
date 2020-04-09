import cv2

cap = cv2.VideoCapture(0)  # open the camera


def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_Canny_edge = cv2.Canny(img_gray_blur, 10, 70)
    ret, mask = cv2.threshold(img_Canny_edge, 70, 255, cv2.THRESH_BINARY)
    # 70 : threshold value, 255: maximum value, cv2.THRESH_BINARY : type
    return mask


while True:
    ret, frame = cap.read()  # read the camera stream
    # ret : hold the value, frame : access the camera with help of frame
    cv2.imshow("Live Video Camera ", sketch(frame))  # show camera / video
    if cv2.waitKey(1) == 13:  # asking code = 13 : close the camera
        break

cap.release()
cv2.destroyAllWindows()
