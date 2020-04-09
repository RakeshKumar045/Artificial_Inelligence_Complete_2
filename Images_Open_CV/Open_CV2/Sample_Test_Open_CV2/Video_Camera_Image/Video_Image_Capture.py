import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
    print("ret ", ret)
    print("Frame ", frame)

else:
    ret = False

img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title("Camera Image")
plt.xticks([])
plt.yticks([])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

cv2.imshow("image :", img)  # error get
cap.release()
