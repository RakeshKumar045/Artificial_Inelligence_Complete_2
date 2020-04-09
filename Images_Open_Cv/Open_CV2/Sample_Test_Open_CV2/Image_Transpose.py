import cv2

img = cv2.imread("sachin.jpg")
img_transpose = cv2.transpose(img)

cv2.imshow("Original image ", img)
cv2.imshow("Transpose image ", img_transpose)

cv2.waitKey(0)
cv2.destroyAllWindows()
