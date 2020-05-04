import cv2
import numpy as np

device = cv2.VideoCapture(0)

while True:
    ret, frame = device.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_range = np.array([110, 50, 51])
    upper_range = np.array([130, 255, 254])
    # 110 : hue(hold color image)
    # 50 : saturation(hold range of color )
    # 51 : value(hold color intensity)

    mask = cv2.inRange(hsv, lower_range, upper_range)  # lower_range & upper_range : use for filter
    # mask only filter blue color & other color  filter keep in hold

    cv2.imshow("Filter  ", mask)
    cv2.imshow("Filter output ", frame)

    if cv2.waitKey(1) == 13:
        break
device.release()
cv2.destroyAllWindows()
