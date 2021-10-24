#!/usr/bin/python3

import time

import tensorflow.keras
import random
import os
from matplotlib import pyplot,numpy as np

from tensorflow.keras.preprocessing.image import load_img, img_to_array

classes      = ['paper','rock','scissors']

base_folder = '/home/rob/rockPaperScissorModel/'

load_model = tensorflow.keras.models.load_model('PRSModelWeights.h5')

pic      = random.choice(os.listdir(base_folder + 'train/scissors/'))
fileName = base_folder + 'train/scissors/' + pic
image    = load_img(fileName, target_size=(150,150),color_mode="rgb")#"rgb" for color mode; "grayscale"
pyplot.imshow(image)
pyplot.show()
photo=img_to_array(image)# convert to numpy array
photo.shape


pic      = random.choice(os.listdir(base_folder + 'train/rock/'))
fileName = base_folder + 'train/rock/' + pic
image    = load_img(fileName, target_size=(150,150),color_mode="rgb")#"rgb" for color mode; "grayscale"
pyplot.imshow(image)
pyplot.show()
photo=img_to_array(image)# convert to numpy array
photo.shape

# now we need to reshape to image to VGG16 required input format
photo = photo.reshape((1, photo.shape[0], photo.shape[1], photo.shape[2]))
photo.shape

print(time.time())
ypred=load_model.predict(photo)
print(time.time())
print('Newest Prediction is')
print(classes[np.argmax(ypred)])
