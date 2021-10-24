#!/bin/python3

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D , Dense , Dropout , Flatten
import numpy as np 
from sklearn.model_selection import train_test_split, StratifiedKFold 
import matplotlib.pyplot as plt 
import cv2 
import pandas as pd 
from glob import glob


from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession


def fix_gpu():
    config = ConfigProto()
    config.gpu_options.allow_growth = True
    session = InteractiveSession(config=config)


fix_gpu()

base_folder = '/home/rob/rockPaperScissorModel/'
paper_subfolder = base_folder + 'paper'
rock_subfolder = base_folder + 'rock'
scissors_subfolder = base_folder + 'scissors'

# finding filenames in respective subfolders
paper_filenames = glob(paper_subfolder + '/*')
rock_filenames = glob(rock_subfolder + '/*')
scissors_filenames = glob(scissors_subfolder + '/*')

# printing filename info 
print("Total {} images found in {} folder".format(len(paper_filenames), paper_subfolder))
print("Total {} images found in {} folder".format(len(rock_filenames), rock_subfolder))
print("Total {} images found in {} folder".format(len(scissors_filenames), scissors_subfolder))



# creating a dataframe for containing the filepaths (complete absolute filepaths) and corresponding class labels
label_names   = ['paper','rock','scissors']
all_filepaths = paper_filenames + rock_filenames + scissors_filenames
all_labels    = [label_names[0]]*len(paper_filenames) + [label_names[1]]*len(rock_filenames) + [label_names[2]]*len(scissors_filenames)
df = pd.DataFrame({'filename':all_filepaths, 'class':all_labels})
print(df.head())
print(df.describe())



# creating a dataframe for containing the filepaths (complete absolute filepaths) and corresponding class labels
label_names   = ['paper','rock','scissors']
all_filepaths = paper_filenames + rock_filenames + scissors_filenames
all_labels    = [label_names[0]]*len(paper_filenames) + [label_names[1]]*len(rock_filenames) + [label_names[2]]*len(scissors_filenames)
df = pd.DataFrame({'filename':all_filepaths, 'class':all_labels})
print(df.head())
print(df.describe())

# performing train, test set splits
train_val_df, test_df = train_test_split(df, test_size=0.1, random_state=0, shuffle=True, stratify=df['class'])
print("Training+Validation set")
print(train_val_df.head())
print(train_val_df.describe())
print('*'*50)
print("Testing set")
print(test_df.head())
print(test_df.describe())
test_df['filename']

import os
import random
import shutil
# defining image folders

classes      = ['paper','rock','scissors']
folders = [paper_subfolder,rock_subfolder,scissors_subfolder]
for i in range(3):
  training = base_folder + 'train/' + classes[i] + '/'
  validation = base_folder + 'validation/' + classes[i] + '/'
  test = base_folder + 'test/' + classes[i] + '/'
  #files = os.listdir(folders[i])
  if not os.path.exists(training): # create a tempory folder 'preview' to save generated images
    os.makedirs(training)
  if not os.path.exists(validation): # create a tempory folder 'preview' to save generated images
    os.makedirs(validation)
  if not os.path.exists(test): # create a tempory folder 'preview' to save generated images
    os.makedirs(test)

  for m in range(int(0.8*700/3)):
    files = [filenames for (filenames) in os.listdir(folders[i])]
    random_file = random.choice(files)
    shutil.copy(os.path.join(folders[i], random_file), training)
  for m in range(int(0.1*700/3)):
    files = [filenames for (filenames) in os.listdir(folders[i])]
    random_file = random.choice(files)
    shutil.copy(os.path.join(folders[i], random_file), validation)    
  for m in range(int(0.1*700/3)):
    files = [filenames for (filenames) in os.listdir(folders[i])]
    random_file = random.choice(files)
    shutil.copy(os.path.join(folders[i], random_file), test)



# Defining ImageDataGenerators for train, val and test sets 
train_data_generator = ImageDataGenerator( rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, rescale=1./255,
                        shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest')
val_data_generator   =  ImageDataGenerator(rescale=1./255)
test_data_generator  =  ImageDataGenerator(rescale=1./255)


# Defining image resolution, batch size, etc 
IMAGE_WIDTH=150
IMAGE_HEIGHT=150
BATCH_SIZE=30


from tensorflow.keras.layers import Input
import random
import matplotlib.pyplot as plt 
from matplotlib.image import imread
from matplotlib import pyplot
from tensorflow.keras.preprocessing.image import load_img, img_to_array

pic      = random.choice(os.listdir(base_folder + 'train/rock/'))
fileName = base_folder + 'train/rock/' + pic
image    = load_img(fileName, target_size=(IMAGE_HEIGHT,IMAGE_WIDTH),color_mode="rgb")#"rgb" for color mode; "grayscale"
pyplot.imshow(image)
pyplot.show()
photo=img_to_array(image)# convert to numpy array

print("##############################################################")
print(photo.shape)


from tensorflow.keras.applications import ResNet50
from sklearn.model_selection import train_test_split, StratifiedKFold
from tensorflow.keras.applications.vgg16 import preprocess_input 
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Conv2D, MaxPooling2D , Dense, Dropout, Flatten, Input, BatchNormalization
from tensorflow.keras.models import Model
# # Defining model architecture for transfer learning 

# # Loading ResNet50 model, initializing with weights trained on the imagenet dataset, input image shape of 
size=150

# constructing the model 

model = Sequential([
    Conv2D(filters=32,kernel_size=(3,3),activation='relu',input_shape = (size, size, 3)),
    MaxPooling2D(pool_size=2) ,# down sampling the output instead of 28*28 it is 14*14i
    Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=2) ,# down sampling the output instead of 28*28 it is 14*14i
    Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=2) ,# down sampling the output instead of 28*28 it is 14*14i
    Dropout(0.2),
    Flatten(), # flatten out the layers
    Dense(32,activation='relu'),
    Dense(3,activation = 'softmax')
    
])
# # compiling the model
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

# # printing model summary
print(model.summary())


# Defining K-fold stratification for train and validation set splits for cross-validation
num_cv_splits = 5
skf = StratifiedKFold(n_splits=num_cv_splits, random_state=0, shuffle=True)
list_train_idxs = []
list_val_idxs   = []
for train_idxs, val_idxs in skf.split(train_val_df['class'], train_val_df['class']):
  list_train_idxs.append(train_idxs)
  list_val_idxs.append(val_idxs)
print(len(list_train_idxs), len(list_val_idxs))
print(len(list_train_idxs[0]), len(list_val_idxs[0]))


# Performing K-fold(5-fold) cross-validation 
train_losses     = []
train_accuracies = []
val_losses       = []
val_accuracies   = []
accResnetList    = []
NUM_EPOCHS = 5
training_data_dir   = base_folder +'train/'
validation_data_dir = base_folder +'validation/'
test_data_dir       = base_folder +'test/'
IMAGE_WIDTH=150
IMAGE_HEIGHT=150
BATCH_SIZE=10

test_data_generator  =  ImageDataGenerator(rescale=1./255)
test_generator = test_data_generator.flow_from_directory(
    test_data_dir,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=1,
    class_mode="categorical",
    shuffle=False)

for i in range(num_cv_splits):
  train_idxs = list_train_idxs[i]
  val_idxs   = list_val_idxs[i]
  train_df = train_val_df.iloc[train_idxs]
  val_df   = train_val_df.iloc[val_idxs]
  
  train_gen = train_data_generator.flow_from_dataframe(train_df, target_size=(IMAGE_HEIGHT, IMAGE_WIDTH), batch_size=BATCH_SIZE)
  val_gen   = val_data_generator.flow_from_dataframe(val_df, target_size=(IMAGE_HEIGHT, IMAGE_WIDTH), batch_size=BATCH_SIZE)
  #modelRes = finetuning_model()
  history = model.fit(train_gen, epochs=NUM_EPOCHS, steps_per_epoch=len(train_df)//BATCH_SIZE, validation_data=val_gen, validation_steps=len(val_df)//BATCH_SIZE) # switching to model.fit since model.fit_generator is being deprecated
  # Check classification accuracy on the test set
  _, accResNet=model.evaluate(test_generator, steps=len(test_generator),verbose=0)
  accResnetList.append(accResNet)
  train_losses.append(history.history['loss'][-1]) 
  val_losses.append(history.history['val_loss'][-1]) 
  train_accuracies.append(history.history['accuracy'][-1]) 
  val_accuracies.append(history.history['val_accuracy'][-1])


# saving and loading the .h5 model
 
# save model
model.save('PRSModelWeights.h5')
print('Model Saved!')


