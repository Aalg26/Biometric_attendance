import cv2
from deepface.extendedmodels import Emotion
from deepface.DeepFace import build_model
import numpy as np

# Initialize emotion model
models = {}
models["emotion"] = build_model("Emotion")

# Define a function to analyze the emotion in an image
def mood(img):
    obj = {}
    
    # Convert the input image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Resize the grayscale image to (48, 48) pixels
    img_gray = cv2.resize(img_gray, (48, 48))
    
    # Add a batch dimension to the image
    img_gray = np.expand_dims(img_gray, axis=0)

    # Predict emotions using the emotion model
    emotion_predictions = models["emotion"].predict(img_gray, verbose=0)[0, :]

    # Calculate the sum of emotion predictions
    sum_of_predictions = emotion_predictions.sum()

    # Initialize an object to store emotion information
    obj["emotion"] = {}

    # Calculate the percentage of each emotion in the predictions
    for i, emotion_label in enumerate(Emotion.labels):
        emotion_prediction = 100 * emotion_predictions[i] / sum_of_predictions
        obj["emotion"][emotion_label] = emotion_prediction

    # Determine the dominant emotion based on the highest prediction
    obj["dominant_emotion"] = Emotion.labels[np.argmax(emotion_predictions)]

    return obj['dominant_emotion']


