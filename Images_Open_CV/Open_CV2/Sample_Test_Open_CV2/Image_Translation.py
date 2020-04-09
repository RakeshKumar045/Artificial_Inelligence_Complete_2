import cv2
import numpy as np

img = cv2.imread("sachin.jpg")

height, width = img.shape[:2]
print("Height : ", height, "and Width : ", width)
quarter_height, quarter_width = height / 4, width / 4
print("Quarter Height : ", quarter_height, "and Quarter Width : ", quarter_width)
# quarter_height, quarter_width = height/2, width/2
# quarter_height, quarter_width = height/2, width/4

# create translation matrix
Translation_Matrix = np.float32([[1, 0, quarter_width],
                                 [0, 1, quarter_height]])

print("Translation_Matrix :", Translation_Matrix)

# create image translation use warpAffine(warpAffine transformation to shift image)
# warpAffine : it's linear image
img_translation = cv2.warpAffine(img, Translation_Matrix, (width, height))
print("img_translation : ", img_translation)
cv2.imshow("original image", img)
cv2.imshow("Translation image ", img_translation)

cv2.waitKey(111111)
cv2.destroyAllWindows()
