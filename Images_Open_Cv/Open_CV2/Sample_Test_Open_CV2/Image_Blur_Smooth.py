import cv2

img = cv2.imread("sachin.jpg")

img_Blur = cv2.blur(img, (3, 3))
print(img_Blur)
img_Gaussian = cv2.GaussianBlur(img, (7, 7), 0)  # it is effective
img_Median = cv2.medianBlur(img, 5)  # it is good effective
img_Bilateral = cv2.bilateralFilter(img, 9, 75, 75)  # it is very good effective

cv2.imshow("original image", img)
cv2.imshow("Blured  img_Blur ", img_Blur)
cv2.imshow("Blured  img_Gaussian ", img_Gaussian)
cv2.imshow("Blured  img_Median ", img_Median)
cv2.imshow("Blured  img_Bilateral ", img_Bilateral)

cv2.waitKey(111111)
cv2.destroyAllWindows()
