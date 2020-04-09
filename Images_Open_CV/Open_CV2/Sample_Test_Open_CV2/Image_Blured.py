import cv2
import numpy as np

img = cv2.imread("sachin.jpg")

kernel_3x3 = np.ones((3, 3), np.float32) / 9  # 3 * 3 = 9
kernel_7x7 = np.ones((7, 7), np.float32) / 49  # 7 * 7 = 49
kernel_11x11 = np.ones((11, 11), np.float32) / 121  # 7 * 7 = 49

print(kernel_3x3)
print(kernel_7x7)

img_blured_3x3 = cv2.filter2D(img, -1, kernel_3x3)
img_blured_7x7 = cv2.filter2D(img, -1, kernel_7x7)
img_blured_11x11 = cv2.filter2D(img, -1, kernel_11x11)

cv2.imshow("original image", img)
cv2.imshow("Blured  image  3x3 ", img_blured_3x3)
cv2.imshow("Blured  image  7x7 ", img_blured_7x7)
cv2.imshow("Blured  image  11x11 ", img_blured_11x11)

cv2.waitKey(111111)
cv2.destroyAllWindows()
