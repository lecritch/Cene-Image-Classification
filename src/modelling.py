from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

def get_preds(model, generator):
    """
    returns an array of class predictions of a given generator.
    model:  keras model created using fit.generator
    generator:  ImageDataGenerator object from keras 
    """
    preds = model.predict_generator(generator)
    preds_max = np.argmax(preds, axis = 1)
    
    return preds_max