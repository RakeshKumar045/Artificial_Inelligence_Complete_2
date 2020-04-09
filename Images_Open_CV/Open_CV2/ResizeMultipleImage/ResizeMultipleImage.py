import cv2
import glob

# Find all images with .jpeg / jpg extension
images = glob.glob("*.jpg")

print(images)
for img in images:
    # Loading all images one by one
    our_image = cv2.imread(img, 0)

    # Resizing all image
    resized_image = cv2.resize(our_image, (300, 300))

    # Show Imaage in a window
    cv2.imshow("Batch", resized_image)
    cv2.imwrite("resized_" + img, resized_image)  # save the image
    cv2.waitKey(500)
    cv2.destroyAllWindows()
