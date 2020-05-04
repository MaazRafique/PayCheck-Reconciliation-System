#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:44:58 2019

@author: maazrafique
"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist
data = mnist.load_data()
(X_train,Y_train),(X_test,Y_test) = mnist.load_data()
X_train = tf.keras.utils.normalize(X_train, axis=1)
X_test = tf.keras.utils.normalize(X_test, axis=1)
#print(X_train[0])
#plt.imshow(X_train[7])

model = tf.keras.models.Sequential()  # a basic feed-forward model
model.add(tf.keras.layers.Flatten())  # takes our 28x28 and makes it 1x784
model.add(tf.keras.layers.Dense(300, activation=tf.nn.relu)) 
model.add(tf.keras.layers.Dense(300, activation=tf.nn.relu)) # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(300, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution

model.compile(optimizer='adam',  # Good default optimizer to start with
              loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
              metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=3)  # train the model

val_loss, val_acc = model.evaluate(X_test, Y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy
#plt.imshow(X_train[0])
model.save('Test.model')
new_model = tf.keras.models.load_model('Test.model')
pred = new_model.predict(X_test)
print(pred)

print(np.argmax(pred[5]))