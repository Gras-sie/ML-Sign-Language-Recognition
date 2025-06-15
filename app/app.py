import os
import re
import base64
from io import BytesIO

from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import string

app = Flask(__name__)

# Load trained model on startup
def load_model():
    global model, LABEL_MAP
    model_path = os.path.join(os.path.dirname(__file__), '../models/asl_cnn_model.h5')
    model = tf.keras.models.load_model(model_path)
    LABEL_MAP = {i: letter for i, letter in enumerate(string.ascii_uppercase)}
    print(f"Model loaded from: {model_path}")

# Preprocess images for inference
def preprocess_image(data, target_size=(224, 224)):
    # Handle base64-encoded images
    if isinstance(data, str) and data.startswith('data:image'):
        header, encoded = data.split(',', 1)
        image_bytes = base64.b64decode(encoded)
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        # FileStorage object
        file_bytes = data.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Resize and normalize
    img = cv2.resize(img, target_size)
    img = img / 255.0
    # Batch dimension
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    image_data = data.get('image')
    img = preprocess_image(image_data)
    preds = model.predict(img)
    index = int(np.argmax(preds))
    letter = LABEL_MAP.get(index, '?')
    return jsonify({'prediction': letter})

@app.route('/classify_image', methods=['POST'])
def classify_image():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No image provided'}), 400
    img = preprocess_image(file)
    preds = model.predict(img)
    index = int(np.argmax(preds))
    letter = LABEL_MAP.get(index, '?')
    return jsonify({'prediction': letter})

if __name__ == '__main__':
    load_model()
    app.run(debug=True)
