import os, shutil
import numpy as np
from keras.preprocessing import image
from PIL import Image

def get_paths(directory):
    buildings_list = os.listdir(directory + '/buildings')
    forest_list = os.listdir(directory + '/forest')
    glacier_list = os.listdir(directory + '/glacier')
    mountain_list = os.listdir(directory + '/mountain')
    sea_list = os.listdir(directory + '/sea')
    street_list = os.listdir(directory + '/street')
    
    buildings_path = [directory + '/buildings/' + img_id for img_id in buildings_list]
    forest_path = [directory + '/forest/' + img_id for img_id in forest_list]
    glacier_path = [directory + '/glacier/' + img_id for img_id in glacier_list]
    mountain_path = [directory + '/mountain/' + img_id for img_id in mountain_list]
    sea_path = [directory + '/sea/' + img_id for img_id in sea_list]
    street_path = [directory + '/street/' + img_id for img_id in street_list]
    
    path_list = buildings_path + forest_path + glacier_path + mountain_path + sea_path + street_path
    
    return path_list


def preprocess_image(path_list):
    output = []
    for img_path in path_list:
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = np.divide(x, 255.0)
        output.append(x)
    return np.vstack(output)