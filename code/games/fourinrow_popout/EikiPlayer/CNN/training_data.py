import pickle
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dropout, Dense, Conv2D, Flatten, MaxPooling2D, Activation, RandomFlip, RandomRotation
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
import tensorflow as tf
print(tf.__version__)
import sklearn as sk
print(sk.__version__)
import matplotlib.pyplot as plt
import cv2
import pickle
import numpy as np
from sklearn.model_selection import train_test_split


pickle_in = open("X.pickle", "rb")
Y = pickle.load(pickle_in)

pickle_in = open("Y.pickle", "rb")
X = pickle.load(pickle_in)

tmpX = []
for k in range(len(X)):
  tmp = np.asarray([[[0,0,0]]*7]*6)
  for i in range(X[k].shape[0]):
    for j in range(X[k].shape[1]):
      if X[k][i][j] == 1:
        tmp[i][j] = [0,0,255]
      elif X[k][i][j] == 2:
        tmp[i][j] = [255,0,0]
      else:
        tmp[i][j] = [0,0,0]
  tmpX.append(tmp)

X = tmpX

X = np.asarray(X)
Y = np.asarray(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.10, random_state=42)
SHAPE = X_train[0].shape


model = Sequential()

model.add(Conv2D(64, (3,3), input_shape = SHAPE, activation = 'relu', padding="same"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128, (3,3), input_shape = SHAPE, activation = 'relu', padding="same"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(256))

model.add(Dense(7, activation = "softmax"))

model.compile(loss = "sparse_categorical_crossentropy",
              optimizer = "adam",
              metrics = ['accuracy'])

history = model.fit(X_train, y_train, batch_size=32, epochs=60, validation_split = 0.2)

plt.style.use('ggplot')
plt.plot(history.history['accuracy'], label="train")
plt.plot(history.history['val_accuracy'], label="validation")
plt.xlabel("Epochs")
plt.legend(loc="lower right")
plt.title("Accuracy")
plt.show()

model.save("cnn_four_in_row.model")