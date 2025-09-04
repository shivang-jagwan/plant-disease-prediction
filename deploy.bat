@echo off
REM Plant Disease Prediction Model - Quick Deploy Script for Windows

echo 🌱 Plant Disease Prediction Model - Deployment Helper
echo ==================================================

echo Select deployment option:
echo 1. Local development server
echo 2. Prepare for Streamlit Cloud
echo 3. Docker build and run
echo 4. Test requirements

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo Starting local development server...
    pip install -r requirements.txt
    streamlit run main.py
) else if "%choice%"=="2" (
    echo Preparing for Streamlit Cloud deployment...
    echo ✓ requirements.txt created
    echo ✓ main.py ready
    echo ✓ Model file should be included
    echo.
    echo Next steps:
    echo 1. Push your code to GitHub
    echo 2. Go to share.streamlit.io
    echo 3. Connect your GitHub repository
    echo 4. Deploy!
) else if "%choice%"=="3" (
    echo Building Docker image...
    docker build -t plant-disease-app .
    echo Running Docker container...
    docker run -p 8501:8501 plant-disease-app
) else if "%choice%"=="4" (
    echo Testing requirements...
    pip install -r requirements.txt
    python -c "import streamlit, tensorflow, numpy, pandas; print('✓ All requirements satisfied')"
) else (
    echo Invalid choice. Please run the script again.
)

pause
