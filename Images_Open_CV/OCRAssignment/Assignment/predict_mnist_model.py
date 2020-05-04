import cv2
import numpy as np
import tensorflow as tf

# Load the model
new_model = tf.keras.models.load_model('mnist_model.h5')

img = cv2.imread("1.png", 0)
img_resize = cv2.resize(img, (28, 28))
print("image resize shape : ", img_resize.shape)

img_dim = np.expand_dims(img_resize, axis=0)
print("img_dim sahpe : ", img_dim.shape)
single_pred = new_model.predict(img_dim)
print(np.argmax(single_pred))
