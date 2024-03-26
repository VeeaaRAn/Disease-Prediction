import base64
import numpy as np
import io
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import imagenet_utils
import keras
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

def get_model():
    global model 
    model = load_model('Model.h5')
    print("model loaded")

def prepare_image(image, target_size):
  image = image.resize(target_size)
  image = img_to_array(image)
  image = np.expand_dims(image, axis=0)
  return tf.keras.applications.mobilenet.preprocess_input(image)

get_model()
@app.route('/')
def start():
    return 'Flask is running'

@app.route('/predict', methods=['POST'])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = prepare_image(image, target_size=(224,224))

    prediction = model.predict(processed_image)
    result = imagenet_utils.decode_predictions(prediction)
    print(result)
    
    response = {
        'prediction': final
    }
    return jsonify(response)