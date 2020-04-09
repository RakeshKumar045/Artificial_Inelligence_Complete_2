import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load the Mnist model
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
print(" X_train type   : ", type(x_train), " X_test type   : ", type(x_test))
print(" Y_train type   : ", type(y_train), "Y_test type   : ", type(y_test))

# Normalization
x_train, x_test = x_train / 255.0, x_test / 255.0
print(x_train.shape)
print(x_test.shape)

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=100)

# evaluate the model
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy is : ", accuracy)
print("Loss is : ", loss)

# Save the model
# model.save('mnist_model.h5')

# Show the model architecture
model.summary()

# Load the model
new_model = tf.keras.models.load_model('mnist_model.h5')

plt.figure(figsize=(100, 12))
for i in range(60):
    plt.subplot(5, 12, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_test[i], cmap=plt.cm.binary)

plt.show()

print(type(x_test))
print("shape :", x_test.shape)
print(type(x_test[0]))
print(x_test[0].shape)
print(x_test[0])

img = cv2.imread("1.png", 0)
img_resize = cv2.resize(img, (28, 28))
print("image resize shape : ", img_resize.shape)

img_dim = np.expand_dims(img_resize, axis=0)
print("img_dim sahpe : ", img_dim.shape)
single_pred = model.predict(img_dim)
print(np.argmax(single_pred))
