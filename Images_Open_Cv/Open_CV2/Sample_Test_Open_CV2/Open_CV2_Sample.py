import cv2

img = cv2.imread("sachin.jpg")  # read the image from folder
cv2.imshow("Sachin normal output", img)  # display image

cv2.imwrite("Sachin_output.jpg", img)  # save the image in the folder as jpg or png
cv2.imwrite("Sachin_output.png", img)

img_shape = img.shape
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
print("shape : ", img_shape)
print("Height pixel values : ", img_height, " & weight pixel values : ", img_width, " & image channel is : ",
      img_channel)
cv2.waitKey(
    0)  # first will display 1st image(normal ), then display 2nd image , if enter any key , then gray image will be display

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Sachin Gray", img_gray)
cv2.waitKey(0)

img_gray_directly = cv2.imread("sachin.jpg",
                               0)  # read the image from folder and 0: means , image convert into gray scale
cv2.imshow("Sachin  gray output", img_gray_directly)  # display gray image
cv2.waitKey(0)

ret, img_binary_normal = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary normal image", img_binary_normal)
cv2.waitKey(0)

ret_gray, img_binary_gray = cv2.threshold(img_gray_directly, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary gray image", img_binary_gray)
cv2.waitKey(0)

ret_inv, img_binary_gray_inv = cv2.threshold(img_gray_directly, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Binary gray image inv", img_binary_gray_inv)
cv2.waitKey(0)

ret_otsu, img_binary_otsu = cv2.threshold(img_gray_directly, 127, 255, cv2.THRESH_OTSU)
cv2.imshow("Binary gray image otsu", img_binary_otsu)
cv2.waitKey(0)

cv2.destroyAllWindows()
