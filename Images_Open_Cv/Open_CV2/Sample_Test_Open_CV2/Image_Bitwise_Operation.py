import cv2
import numpy as np

# sequae
sequare = np.zeros((300, 300), np.uint8)
cv2.rectangle(sequare, (50, 50), (250, 250), 255, -1)
cv2.imshow("Seqaure ", sequare)

# Eclipse
eclipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(eclipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Eclipse ", eclipse)

# And Image
img_And = cv2.bitwise_and(sequare, eclipse)
cv2.imshow("And ", img_And)

# Or Image
img_Or = cv2.bitwise_or(sequare, eclipse)
cv2.imshow("Or ", img_Or)

# Xor Image
img_Xor = cv2.bitwise_xor(sequare, eclipse)
cv2.imshow("Xor ", img_Xor)

# Not Image
img_Not = cv2.bitwise_not(sequare)
cv2.imshow("Not ", img_Not)

cv2.waitKey(0)
cv2.destroyAllWindows()
