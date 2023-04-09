import numpy as np
import tensorflow as tf
from keras import layers, models
from keras.optimizers import SGD
import os
import cv2
import random
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



train_data = tf.keras.utils.image_dataset_from_directory("data",validation_split=0.2,seed=123,subset="training",batch_size=5,image_size=(200,200))
val_data = tf.keras.utils.image_dataset_from_directory("data",validation_split=0.2,seed=123,subset="validation",batch_size=5,image_size=(200,200))

length = len(train_data.class_names)

AUTOTUNE = tf.data.AUTOTUNE
train_data = train_data.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_data = val_data.cache().prefetch(buffer_size=AUTOTUNE)


model = models.Sequential()
model.add(layers.Rescaling(1./255, input_shape=(200, 200, 3)))
model.add(layers.Conv2D(256, 3, activation='relu', input_shape=(200,200,3)))
model.add(layer=layers.MaxPool2D())
model.add(layers.Conv2D(128, 3, activation='relu'))
model.add(layer=layers.MaxPool2D())
model.add(layers.Flatten())
model.add(layers.Dense(256,activation='relu'))
model.add(layers.Dense(128,activation='sigmoid'))
model.add(layers.Dense(length))
# opt = SGD(learning_rate=0.005)
model.compile(optimizer='adam',loss="sparse_categorical_crossentropy",metrics=['accuracy'])
history = model.fit(train_data, epochs = 10, validation_data = val_data)
model.save("model.h5")

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(10)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
