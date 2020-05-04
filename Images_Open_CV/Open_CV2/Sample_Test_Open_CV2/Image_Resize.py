import cv2

img = cv2.imread("sachin.jpg")
img_resize = cv2.resize(img, None, fx=0.75, fy=0.75)
img_resize_2 = cv2.resize(img, None, fx=1.2, fy=1.2)
# img_resize_3 = cv2.resize(img, 200, 300) # error


img_resize_scaled = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
img_resize_skewed = cv2.resize(img, (900, 400), interpolation=cv2.INTER_CUBIC)

cv2.imshow("original image ", img)
cv2.imshow("Linear Interplotation Resize image ", img_resize)
cv2.imshow("Resize image2 ", img_resize_2)
# cv2.imshow("Resize image3 ", img_resize_3)


cv2.imshow("Resize img_resize_scaled ", img_resize_scaled)
cv2.imshow("Resize img_resize_skewed ", img_resize_skewed)

cv2.waitKey(0)
cv2.destroyAllWindows()
