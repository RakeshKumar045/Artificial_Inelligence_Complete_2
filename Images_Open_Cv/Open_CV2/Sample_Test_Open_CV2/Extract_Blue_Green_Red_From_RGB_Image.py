import cv2
import numpy as np

img = cv2.imread("sachin.jpg")
cv2.imshow("Original Image", img)
cv2.waitKey(0)

B, G, R = cv2.split(img)  # It's BGR (Not RGB)
create_image_zeros_types_matrix = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow("Red Image", cv2.merge([create_image_zeros_types_matrix, create_image_zeros_types_matrix, R]))
cv2.imshow("Green Image", cv2.merge([create_image_zeros_types_matrix, G, create_image_zeros_types_matrix]))
cv2.imshow("Blue Image", cv2.merge([B, create_image_zeros_types_matrix, create_image_zeros_types_matrix]))

cv2.waitKey(0)
cv2.destroyAllWindows()
