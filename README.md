# 🌱 Plant Disease Recognition System

A machine learning-powered web application for detecting plant diseases from images using deep learning.

## 🚀 Live Demo
**[🌐 Try the Live App](https://plant-disease-prediction-1-26m6.onrender.com)**

Deployed on Render - Click the link above to use the plant disease detection system!

## ✨ Features

- Real-time plant disease detection
- Support for 38+ disease classes  
- User-friendly Streamlit interface
- High accuracy predictions with confidence scores
- Optimized for web deployment

## 🛠️ Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/shivang-jagwan/plant-disease-prediction.git
   cd plant-disease-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run main.py
   ```

## 📊 Model Information

- **Framework**: TensorFlow/Keras
- **Input size**: 128x128 pixels
- **Classes**: 38 plant disease categories
- **Model file**: Disease_classification_model.keras (89MB)

## 🌐 Deployment

This application is configured for deployment on Render with:
- Automatic deployments from GitHub
- Optimized for serverless deployment
- Free tier compatible

## 📁 Project Structure

```
├── main.py                           # Streamlit application
├── Disease_classification_model.keras # Trained ML model
├── requirements.txt                  # Python dependencies  
├── render.yaml                      # Render configuration
├── .streamlit/config.toml          # Streamlit configuration
└── 47ec2dbb0cf87c01830f03e5445956eed6fa2d02.jpg # Background image
```

## 🤝 Contributing

Feel free to open issues and submit pull requests to improve the application!
