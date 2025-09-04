from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)

# Load your Keras model
model = tf.keras.models.load_model('model/Disease_classification_model.keras')

# Load the recommendation data
with open('recommendation.json', 'r', encoding='utf-8') as f:
    recommendations = json.load(f)

# Class names for prediction (Mapping to Hindi names)
class_names = [
    ("Apple", "सेब", "Apple Scab", "सेब की स्कैब बीमारी"),
    ("Apple", "सेब", "Black Rot", "ब्लैक रॉट"),
    ("Apple", "सेब", "Cedar Apple Rust", "देवदार सेब रस्ट"),
    ("Apple", "सेब", "Healthy", "स्वस्थ"),
    ("Blueberry", "ब्लूबेरी", "Healthy", "स्वस्थ"),
    ("Cherry", "चेरी", "Powdery Mildew", "पाउडरी मिल्ड्यू"),
    ("Cherry", "चेरी", "Healthy", "स्वस्थ"),
    ("Corn", "मक्का", "Cercospora Leaf Spot", "सर्कोस्पोरा लीफ स्पॉट"),
    ("Corn", "मक्का", "Common Rust", "कॉमन रस्ट"),
    ("Corn", "मक्का", "Northern Leaf Blight", "नॉर्दर्न लीफ ब्लाइट"),
    ("Corn", "मक्का", "Healthy", "स्वस्थ"),
    ("Grape", "अंगूर", "Black Rot", "ब्लैक रॉट"),
    ("Grape", "अंगूर", "Esca (Black Measles)", "एसका (ब्लैक मीजल्स)"),
    ("Grape", "अंगूर", "Leaf Blight", "लीफ ब्लाइट"),
    ("Grape", "अंगूर", "Healthy", "स्वस्थ"),
    ("Orange", "संतरा", "Citrus Greening", "साइट्रस ग्रीनिंग"),
    ("Peach", "आड़ू", "Bacterial Spot", "बैक्टीरियल स्पॉट"),
    ("Peach", "आड़ू", "Healthy", "स्वस्थ"),
    ("Pepper", "शिमला मिर्च", "Bacterial Spot", "बैक्टीरियल स्पॉट"),
    ("Pepper", "शिमला मिर्च", "Healthy", "स्वस्थ"),
    ("Potato", "आलू", "Early Blight", "अर्ली ब्लाइट"),
    ("Potato", "आलू", "Late Blight", "लेट ब्लाइट"),
    ("Potato", "आलू", "Healthy", "स्वस्थ"),
    ("Raspberry", "रास्पबेरी", "Healthy", "स्वस्थ"),
    ("Soybean", "सोयाबीन", "Healthy", "स्वस्थ"),
    ("Squash", "स्क्वाश", "Powdery Mildew", "पाउडरी मिल्ड्यू"),
    ("Strawberry", "स्ट्रॉबेरी", "Leaf Scorch", "लीफ स्कॉर्च"),
    ("Strawberry", "स्ट्रॉबेरी", "Healthy", "स्वस्थ"),
    ("Tomato", "टमाटर", "Bacterial Spot", "बैक्टीरियल स्पॉट"),
    ("Tomato", "टमाटर", "Early Blight", "अर्ली ब्लाइट"),
    ("Tomato", "टमाटर", "Late Blight", "लेट ब्लाइट"),
    ("Tomato", "टमाटर", "Leaf Mold", "लीफ मोल्ड"),
    ("Tomato", "टमाटर", "Septoria Leaf Spot", "सेप्टोरिया लीफ स्पॉट"),
    ("Tomato", "टमाटर", "Spider Mites", "स्पाइडर माइट्स"),
    ("Tomato", "टमाटर", "Target Spot", "टारगेट स्पॉट"),
    ("Tomato", "टमाटर", "Yellow Leaf Curl Virus", "येलो लीफ कर्ल वायरस"),
    ("Tomato", "टमाटर", "Tomato Mosaic Virus", "टोमैटो मोज़ेक वायरस"),
    ("Tomato", "टमाटर", "Healthy", "स्वस्थ")
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    
    filename = secure_filename(file.filename)
    file_path = os.path.join('static', 'uploads', filename)
    file.save(file_path)

   
    image = tf.keras.preprocessing.image.load_img(file_path, target_size=(128, 128))
    input_array = tf.keras.preprocessing.image.img_to_array(image)
    input_array = np.array([input_array])  

    
    prediction = model.predict(input_array)
    result_index = np.argmax(prediction)
    confidence_score = np.max(prediction) * 100  # Convert to percentage

    # Get the plant and disease details
    plant_eng, plant_hin, disease_eng, disease_hin = class_names[result_index]

    # Return the result
    return jsonify({
        'plant_name_eng': plant_eng,
        'plant_name_hin': plant_hin,
        'disease_eng': disease_eng,
        'disease_hin': disease_hin,
        'confidence': float(confidence_score),
        'image_url': f'/static/uploads/{filename}'
    })

# Recommendation route
@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    plant_eng = data.get('plant_name_eng')
    disease_eng = data.get('disease_eng')

    # Check if the plant exists in the recommendations
    if plant_eng in recommendations:
        # Check if the disease exists for the plant
        if disease_eng in recommendations[plant_eng]:
            recommendation = recommendations[plant_eng][disease_eng]["treatment"]
        else:
            recommendation = "No specific recommendation available for this disease."
    else:
        recommendation = "No recommendations available for this plant."

    return jsonify({
        'plant_name_eng': plant_eng,
        'disease_eng': disease_eng,
        'recommendation': recommendation
    })
if __name__ == '__main__':
    os.makedirs(os.path.join('static', 'uploads'), exist_ok=True)
    app.run(debug=True)