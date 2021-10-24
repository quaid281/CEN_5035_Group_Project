#!/usr/bin/python3

import tensorflow.keras
import random
import os
from matplotlib import pyplot,numpy as np
import sys

from tensorflow.keras.preprocessing.image import load_img, img_to_array


classes      = ['paper','rock','scissors']

def predictImage(img, model, classes):
    image = img_to_array(img)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    ypred = model.predict(image)

    return classes[np.argmax(ypred)]


def loadModel():
    return tensorflow.keras.models.load_model('/home/rob/gits/CEN_5035_Group_Project/tools/model/PRSModelWeights.h5')

def loadClasses():
    return classes
