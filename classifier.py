# model.py
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import io
import numpy as np

class classify:
    def __init__(self, model_path='Model.h5'):
        self.model = load_model(model_path)
        self.class_names = ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight','Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
        'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tommato_mosaic_virus', 'Tomato___healthy']  # Replace with your actual class names

    def image_preprocessing(self, image_data):
        img = image.load_img(image_data, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x

    def predict(self, image_data):
        try:
            x = self.image_preprocessing(image_data)
            prediction = self.model.predict(x)
            predicted_class_index = np.argmax(prediction)
            predicted_class = self.get_class_name(predicted_class_index)
            print(f"Predicted Class Index: {predicted_class_index}")
            print(f"Predicted Class Name: {predicted_class}")
            return predicted_class

        except Exception as e:
            print(f"Error predicting class for image: {e}")
            return None

    def get_class_name(self, class_index):
        return self.class_names[class_index]

