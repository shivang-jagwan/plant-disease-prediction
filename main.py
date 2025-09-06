import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import os

# Set page config first
st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for background and styling
st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background: url("47ec2dbb0cf87c01830f03e5445956eed6fa2d02.jpg");  /* Insert your background image URL here */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* Center title and add color */
    h1, h2, h3 {
        text-align: center;
        color: #ffffff;  /* White text */
        font-weight: bold;
    }

    /* Custom button styling */
    .stButton>button {
        background-color: #28a745; /* Green button */
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px;
    }
    
    /* Image Styling */
    .uploaded-image {
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        max-width: 300px; /* Smaller image */
        display: block;
        margin: auto;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Navigation as Header
st.markdown("<h2>🌱 Plant Disease Recognition System</h2>", unsafe_allow_html=True)
nav_options = ["Home", "About", "Disease Recognition"]
selected_page = st.radio("Navigate to:", nav_options, horizontal=True)

# Load model once and cache it
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('Disease_classification_model.keras')

# TensorFlow Model Prediction
def model_prediction(test_image):
    model = load_model()
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128,128))
    input_array = tf.keras.preprocessing.image.img_to_array(image)
    input_array = np.array([input_array])  # Convert single image to batch
    prediction = model.predict(input_array)
    result_index = np.argmax(prediction)
    confidence_score = np.max(prediction) * 100  # Convert to percentage
    return result_index, confidence_score

# Home Page
if selected_page == "Home":
    st.header("🌿 Welcome to Plant Disease Recognition System")
    image_path = "47ec2dbb0cf87c01830f03e5445956eed6fa2d02.jpg"  # Replace with your image
    st.image(image_path, use_container_width=True)
    
    st.markdown("""
    Welcome to the **Plant Disease Recognition System**! 🌾🛠️  
    This system helps farmers identify plant diseases instantly.  
    Just **upload a plant image**, and our AI model will **detect diseases** accurately! ✅  
    """, unsafe_allow_html=True)

# About Page
elif selected_page == "About":
    st.header("📌 About the Project")
    st.markdown("""
    #### 🌾 **Dataset Overview**  
    This dataset consists of 87K+ images of **healthy and diseased crops**, categorized into **38 different classes**.
    
    ✅ **Total Images:** 87,000+  
    ✅ **Training Set:** 70,295 images  
    ✅ **Validation Set:** 17,572 images  
    ✅ **Test Set:** 33 images  
    
    Our AI model has been trained on these datasets to provide **fast and accurate plant disease detection**! 🚀
    """, unsafe_allow_html=True)

# Disease Recognition Page
elif selected_page == "Disease Recognition":
    st.header("🧐 Disease Recognition System")
    test_image = st.file_uploader("📷 Upload an Image of the Plant")

    # Display Image
    if test_image:
        st.image(test_image, width=300, use_column_width=False, caption="Uploaded Image", output_format="auto")

    # Prediction Button
    if st.button("🔍 Predict"):
        if test_image:
            result_index, confidence_score = model_prediction(test_image)
            
            class_name = [
                'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                'Tomato___healthy'
            ]

            disease_detected = class_name[result_index]
            st.success(f"🌿 **Detected Disease:** {disease_detected}")
            st.success(f"📊 **Confidence Score:** {confidence_score:.2f}%")
        else:
            st.warning("⚠ Please upload an image first.")
