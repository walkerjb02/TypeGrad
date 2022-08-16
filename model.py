import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Flatten, Conv2D, Dense, MaxPooling2D
from keras.optimizers import SGD
from utils import Utils
from transformations import Transformations
import matplotlib.pyplot as plt

num_classes = 10
input_shape = (56, 56, 1)

def load_train_data():
    from emnist import extract_training_samples, extract_test_samples
    x_train, y_train = extract_training_samples('byclass')
    x_test, y_test = extract_test_samples('byclass')
    return ((x_train, y_train), (x_test, y_test))

def apply_to_train(array):
    idx = 0
    output_array = np.zeros((array.shape[0], 56, 56))
    while idx < len(array):
        pilarray = Utils().to_PIL(array[idx])
        resizedpil = Transformations().enlarge_image(pilarray)
        backtoarray = np.array(resizedpil)
        output_array[idx] = backtoarray
        idx += 1
    return output_array


x_train = apply_to_train(load_train_data()[0][0])
x_train = x_train.astype("float32") / 255
x_train = np.expand_dims(x_train, -1)

x_test = apply_to_train(load_train_data()[1][0])
x_test = x_test.astype("float32") / 255
x_test = np.expand_dims(x_test, -1)

print("x_test shape:", x_test.shape)
print(x_test.shape[0], "test samples")
y_train = keras.utils.to_categorical(load_train_data()[0][1], num_classes)
y_test = keras.utils.to_categorical(load_train_data()[1][1], num_classes)

def model():
    model = keras.Sequential(
        [
            keras.Input(shape=input_shape),
            keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
            keras.layers.MaxPooling2D(pool_size=(2, 2)),
            keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            keras.layers.MaxPooling2D(pool_size=(2, 2)),
            keras.layers.Flatten(),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(num_classes, activation="softmax"),
        ]
    )

    model.summary()
    batch_size = 128
    epochs = 15

    model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=1e-2), metrics=["accuracy"])

    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
    score = model.evaluate(x_test, y_test, verbose=0)
    model.save(r'C:\Users\gsbaw\PycharmProjects\TypeGrad\Lib')
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])
