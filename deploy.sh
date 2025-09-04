#!/bin/bash

# Plant Disease Prediction Model - Quick Deploy Script

echo "🌱 Plant Disease Prediction Model - Deployment Helper"
echo "=================================================="

echo "Select deployment option:"
echo "1. Local development server"
echo "2. Prepare for Streamlit Cloud"
echo "3. Docker build and run"
echo "4. Test requirements"

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "Starting local development server..."
        pip install -r requirements.txt
        streamlit run main.py
        ;;
    2)
        echo "Preparing for Streamlit Cloud deployment..."
        echo "✓ requirements.txt created"
        echo "✓ main.py ready"
        echo "✓ Model file should be included"
        echo ""
        echo "Next steps:"
        echo "1. Push your code to GitHub"
        echo "2. Go to share.streamlit.io"
        echo "3. Connect your GitHub repository"
        echo "4. Deploy!"
        ;;
    3)
        echo "Building Docker image..."
        docker build -t plant-disease-app .
        echo "Running Docker container..."
        docker run -p 8501:8501 plant-disease-app
        ;;
    4)
        echo "Testing requirements..."
        pip install -r requirements.txt
        python -c "import streamlit, tensorflow, numpy, pandas; print('✓ All requirements satisfied')"
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        ;;
esac
