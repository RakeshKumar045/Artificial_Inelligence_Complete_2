import cv2

img = cv2.imread("sachin.jpg")
img_smaller = cv2.pyrDown(img)  # convert into smaller image
img_larger = cv2.pyrUp(img)  # convert into larger image

cv2.imshow("Original Image", img)
cv2.imshow("Smaller Image", img_smaller)
cv2.imshow("Larger Image", img_larger)

cv2.waitKey(0)
cv2.destroyAllWindows()
