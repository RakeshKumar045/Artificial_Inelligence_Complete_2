import cv2

img = cv2.imread("sachin.jpg")

height, width = img.shape[:2]
print("Height : ", height, "and Width : ", width)
# quarter_height, quarter_width = height/4, width/4
quarter_height, quarter_width = height / 2, width / 2
print("Quarter Height : ", quarter_height, "and Quarter Width : ", quarter_width)

# 70 : 70 degree and .5 : scaling factor
Rotation_Matrix = cv2.getRotationMatrix2D((quarter_width, quarter_height), 70, .5)
Rotation_Matrix1 = cv2.getRotationMatrix2D((quarter_width, quarter_height), 120, .75)
Rotation_Matrix2 = cv2.getRotationMatrix2D((quarter_width, quarter_height), 70, 1)
print("Rotation_Matrix : ", Rotation_Matrix)

# create image translation use warpAffine(warpAffine transformation to shift image)
# warpAffine : it's linear image
img_rotation = cv2.warpAffine(img, Rotation_Matrix, (width, height))
img_rotation1 = cv2.warpAffine(img, Rotation_Matrix1, (width, height))
img_rotation2 = cv2.warpAffine(img, Rotation_Matrix2, (width, height))
cv2.imshow("original image", img)
cv2.imshow("Translation image ", img_rotation)
cv2.imshow("Translation image1 ", img_rotation1)
cv2.imshow("Translation image2 ", img_rotation2)

cv2.waitKey(111111)
cv2.destroyAllWindows()
