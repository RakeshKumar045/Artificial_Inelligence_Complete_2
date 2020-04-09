import cv2

img = cv2.imread("sachin.jpg")
height, width = img.shape[:2]
print("Height : ", height, "and Width : ", width)

start_row, start_col = int(height * .45), int(width * .45)  # start pixel co-ordinate(top->left, of cropping rectangle)
end_row, end_col = int(height * .55), int(width * .55)  # end pixel co-ordinate(bottm -> right, of cropping rectangle)

img_cropped = img[start_row: start_col, end_row: end_col]
cv2.imshow("original image", img)
cv2.imshow("Translation image ", img_cropped)

cv2.waitKey(111111)
cv2.destroyAllWindows()
