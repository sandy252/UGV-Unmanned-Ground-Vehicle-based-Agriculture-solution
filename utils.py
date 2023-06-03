from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import tensorflow as tf
import pickle
from PIL import Image


CLASS_NAMES = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight',
               'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight',
               'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite',
               'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']


def load_classifier():
    """
    This function loads the pre-trained model from the root.
    :return: returns the crop recommendation classifier
    """
    with open("classifier.pkl", "rb") as file:
        classifier = pickle.load(file)
    return classifier


def load_model():
    """
    This function loads the CNN pre-trained CNN classifier from root.
    :return: returns the classifier
    """
    model = tf.keras.models.load_model("model.h5")
    return model


def classify(list):
    classifier = load_classifier()
    result = classifier.predict(list)
    return result


def predict(image, model):
    """
    This function is responsible for taking the raw image of a leaf and performing some preprocessing, and then finally
    classifying the leaf in terms of the classes.
    :param image: raw image of a leaf that has to be predicted.
    :param model: the predictor model which predicts the disease in the image
    :return: returns the status of the leaf along with the confidence of its prediction
    """
    image = Image.open(image)
    new_image = image.resize((256, 256))
    # st.image(image)
    # image = img_to_array(image)
    new_image = np.asarray(new_image)  # Since our model accepts inputs in the form of tensors
    img_batch = np.expand_dims(new_image, 0)  # Adding fourth dim as model accepts inputs in batch
    predictions = model.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]  # finds the index  of max prob amongst CLASSES
    confidence = np.max(predictions[0])

    return predicted_class, confidence
