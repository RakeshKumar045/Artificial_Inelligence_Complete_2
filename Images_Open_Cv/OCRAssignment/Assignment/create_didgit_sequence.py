import cv2
import numpy as np
from PIL import Image, ImageDraw


def create_digit_sequence(number, image_width, min_spacing, max_spacing):
    default_height = 120
    image = Image.new('RGB', (image_width, default_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    avg_spacing = np.mean([min_spacing, max_spacing])
    space = 0
    for digit in number:
        space = space + avg_spacing
        (x, y) = (space, 50)
        color = 'rgb(0, 0, 0)'
        draw.text((x, y), digit, fill=color)

    image.save('digit.png')

    numpy_image = np.array(image)
    return numpy_image


val = create_digit_sequence("1234", 400, 2, 10)
img = cv2.imread('digit.png')
cv2.imshow("Digit Sequene", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
