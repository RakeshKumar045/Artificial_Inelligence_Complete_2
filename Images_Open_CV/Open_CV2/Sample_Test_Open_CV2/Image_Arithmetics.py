import cv2
import numpy as np

img = cv2.imread("sachin.jpg")

img_Arithmetics = np.ones(img.shape, dtype="uint8") * 150
img_Arithmetics_1 = np.zeros(img.shape, dtype="uint8") + 150

added = cv2.add(img, img_Arithmetics)
subtracted = cv2.subtract(img, img_Arithmetics)
divided = cv2.divide(img, img_Arithmetics)
multiplied = cv2.multiply(img, img_Arithmetics)

added_1 = cv2.add(img, img_Arithmetics_1)
subtracted_1 = cv2.subtract(img, img_Arithmetics_1)
divided_1 = cv2.divide(img, img_Arithmetics_1)
multiplied_1 = cv2.multiply(img, img_Arithmetics_1)

cv2.imshow("original image", img)
cv2.imshow("Image  Arithmetic Added", added)
cv2.imshow("Image  Arithmetic subtracted", subtracted)
cv2.imshow("Image  Arithmetic Divided", divided)
cv2.imshow("Image  Arithmetic Multiplied", multiplied)

cv2.imshow("Image  Arithmetic Added_1", added_1)
cv2.imshow("Image  Arithmetic subtracted_1", subtracted_1)
cv2.imshow("Image  Arithmetic Divided_1", divided_1)
cv2.imshow("Image  Arithmetic Multiplied_1", multiplied_1)

cv2.waitKey(111111)
cv2.destroyAllWindows()
