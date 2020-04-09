import cv2

# img_Gray = cv2.imread("sachin.jpg")
img_Gray = cv2.imread("sachin.jpg", 0)
# height, width = img_Gray.shape[:2]
height, width = img_Gray.shape
print(height, width)

# Extract Slop Edge
sobel_x = cv2.Sobel(img_Gray, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img_Gray, cv2.CV_64F, 0, 1, ksize=5)

img_soble_Or = cv2.bitwise_or(sobel_x, sobel_y)  # addition of 2 of images
img_soble_And = cv2.bitwise_and(sobel_x, sobel_y)  # intersection of 2 of images
img_soble_XOr = cv2.bitwise_xor(sobel_x, sobel_y)  # opposite of addition of 2 of images
img_soble_Not = cv2.bitwise_not(sobel_x, sobel_y)  # not of 2 of images

img_Laplacian = cv2.Laplacian(img_Gray, cv2.CV_64F)
img_Canny = cv2.Canny(img_Gray, 20, 170)  # VVI, use 2 threshold value (20, 170)

cv2.imshow("original image", img_Gray)
cv2.imshow("sobel_x image x ", sobel_x)
cv2.imshow("sobel_y image y ", sobel_y)

cv2.imshow("Image img_soble_Or ", img_soble_Or)
cv2.imshow("Image img_soble_And ", img_soble_And)
cv2.imshow("Image img_soble_XOr ", img_soble_XOr)
cv2.imshow("Image img_soble_Not ", img_soble_Not)

cv2.imshow("image img_Laplacian ", img_Laplacian)
cv2.imshow("image img_Canny ", img_Canny)

cv2.waitKey(111111)
cv2.destroyAllWindows()
