import base64
import cv2
import io
import numpy as np
import text_to_image
from PIL import Image
from PIL import ImageDraw


def test2():
    encoded_image_path = text_to_image.encode("Hello World!", "image.png")
    encoded_image_path = text_to_image.encode_file("input_text_file.txt", "output_image.png")

    decoded_text = text_to_image.decode("encoded_image.png")
    decoded_file_path = text_to_image.decode_to_file("encoded_image.png", "output_text_file.txt")


# Take in base64 string and return cv image
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)


def create_digit_sequence(number, image_width, min_spacing, max_spacing):
    """ A function that create an image representing the given number,
    with random spacing between the digits.
    Each digit is randomly sampled from the MNIST dataset_D.
    Returns an NumPy array representing the image.
    Parameters
    ----------
    number: str
    A string representing the number, e.g. "14543"
    image_width: int
    The image width (in pixel).
    min_spacing: int
    The minimum spacing between digits (in pixel).
    max_spacing: int
    The maximum spacing between digits (in pixel).
    """
    print("hiii")

    # encoded_image_path = text_to_image.encode("Hello World!", "image.png")
    img = cv2.imread("image.png")
    cv2.imshow("Dispaly image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test1():
    img = Image.new('RGB', (200, 100))
    d = ImageDraw.Draw(img)
    d.text((20, 20), 'Hello', fill=(255, 0, 0))
    print("ok")


# test1()
stringToRGB("12345")
# create_digit_sequence("1234", 120, 2, 5)
