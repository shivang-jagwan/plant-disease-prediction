# Deployment Guide

## Quick Deployment Options

### 1. Streamlit Community Cloud (Recommended - Free)

**Steps:**
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your repository
5. Set main file path: `main.py`
6. Deploy!

**Requirements:**
- GitHub repository (public)
- All files including `requirements.txt` and `main.py`

### 2. Heroku Deployment

**Steps:**
1. Install Heroku CLI
2. Create Heroku app:
   ```bash
   heroku create your-app-name
   ```
3. Push to Heroku:
   ```bash
   git add .
   git commit -m "Deploy plant disease app"
   git push heroku main
   ```

**Files needed:**
- `Procfile` ✓
- `requirements.txt` ✓
- `runtime.txt` ✓

### 3. Railway Deployment

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Select your repo
4. Railway will auto-detect and deploy

### 4. Render Deployment

**Steps:**
1. Go to [render.com](https://render.com)
2. Connect GitHub
3. Create new Web Service
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `streamlit run main.py --server.port=$PORT --server.address=0.0.0.0`

### 5. Docker Deployment

**Local Docker:**
```bash
docker build -t plant-disease-app .
docker run -p 8501:8501 plant-disease-app
```

**Docker Compose:**
```bash
docker-compose up --build
```

### 6. Google Cloud Platform

**Steps:**
1. Enable Cloud Run API
2. Build and deploy:
   ```bash
   gcloud run deploy plant-disease-app --source . --platform managed --region us-central1 --allow-unauthenticated
   ```

### 7. AWS Deployment (EC2)

**Steps:**
1. Launch EC2 instance
2. Install dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install -r requirements.txt
   ```
3. Run application:
   ```bash
   streamlit run main.py --server.port=8501 --server.address=0.0.0.0
   ```
4. Configure security group to allow port 8501

## Environment Variables

For production deployment, consider setting:
- `STREAMLIT_SERVER_PORT`: Port number (default 8501)
- `STREAMLIT_SERVER_ADDRESS`: Address (0.0.0.0 for production)

## Important Notes

1. **Model File**: Ensure `Disease_classification_model.keras` is included in deployment
2. **Image File**: Make sure `47ec2dbb0cf87c01830f03e5445956eed6fa2d02.jpg` is accessible
3. **Memory**: The TensorFlow model requires sufficient memory (recommend 512MB+)
4. **Build Time**: Initial deployment may take longer due to TensorFlow installation

## Troubleshooting

**Common Issues:**
- Model file not found: Ensure the `.keras` file is in the repository
- Memory errors: Use platforms with sufficient RAM
- Slow loading: TensorFlow models take time to load initially

**Performance Tips:**
- Use model caching with `@st.cache_resource`
- Optimize image preprocessing
- Consider model quantization for smaller deployments
