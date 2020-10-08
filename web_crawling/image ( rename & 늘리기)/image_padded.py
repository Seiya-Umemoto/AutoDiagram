from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# image가 저장되어 있는 folder명 기입
path_1 = "image"
files = glob.glob(path_1 + '/*.jpg')

# image를 저장하는 folder명 기입
path_2 = "save"
if os.path.isdir(path_2) == False:
  os.mkdir(path_2)

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

for i, file in enumerate(files):
  
    # image의 shape을 4차원으로 바꾸기 
    img = load_img(file)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
  
    # 20장의 image를 합성 
    g = datagen.flow(x, batch_size=1, save_to_dir=path_2, save_prefix='img', save_format='jpg')
    for i in range(20):
        batch = g.next()