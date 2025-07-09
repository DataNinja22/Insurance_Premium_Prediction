# Insurance Premium Prediction API

A FastAPI-based machine learning application for predicting insurance premiums with a clean, professional architecture.

## 🏗️ Project Structure

```
📁 Insurance_Premium_Docker/
├── 📁 src/                     # Main source code
│   ├── 📁 api/                 # FastAPI endpoints and routes
│   │   ├── main.py             # Main FastAPI application
│   │   └── __init__.py
│   ├── 📁 models/              # ML models and prediction logic
│   │   ├── predict.py          # Prediction functions
│   │   ├── model.pkl           # Trained model
│   │   └── __init__.py
│   ├── 📁 schemas/             # Pydantic models for request/response
│   │   ├── user_input.py       # Input validation schema
│   │   ├── prediction_response.py # Response schema
│   │   └── __init__.py
│   ├── 📁 config/              # Configuration files
│   │   ├── city_tier.py        # City tier mappings
│   │   └── __init__.py
│   ├── 📁 utils/               # Utility functions
│   │   └── __init__.py
│   └── __init__.py
├── 📁 ui/                      # Streamlit frontend
│   ├── ui.py                   # Main Streamlit application
│   └── __init__.py
├── 📁 notebooks/               # Jupyter notebooks for development
│   └── fastapi_ml_model.ipynb  # Model development notebook
├── 📁 scripts/                 # Deployment and utility scripts
│   └── deploy.py               # Deployment automation
├── 📁 tests/                   # Test files
│   ├── test_api.py             # API endpoint tests
│   └── __init__.py
├── 📁 docs/                    # Documentation
├── 📁 data/                    # Dataset files
│   └── insurance.csv           # Training dataset
├── requirements.txt            # All dependencies
├── Dockerfile                  # Multi-stage Docker configuration
├── docker-compose.yml          # Docker Compose setup
├── main.py                     # Main application entry point
├── start.sh                    # Linux/Mac startup script
├── start.bat                   # Windows startup script
└── README.md                   # This file
```

## 🚀 Quick Start

### Option 1: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start backend
cd src && python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# Start frontend (in new terminal)
cd ui && streamlit run ui.py --server.port 8501 --server.address 0.0.0.0
```

### Option 2: Using Main Entry Point
```bash
# Install dependencies
pip install -r requirements.txt

# Start backend only
python main.py
```

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)
```bash
# Start both services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Manual Docker Build
```bash
# Build backend
docker build --target backend -t insurance-api .
docker run -d -p 8000:8000 insurance-api

# Build frontend
docker build --target frontend -t insurance-ui .
docker run -d -p 8501:8501 insurance-ui

# Build development environment
docker build --target development -t insurance-dev .
docker run -it -p 8000:8000 -p 8501:8501 insurance-dev
```

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message and API info |
| GET | `/health` | Health check and model status |
| POST | `/predict` | Insurance premium prediction |

### Example API Usage

**Request:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "weight": 70.0,
    "height": 1.75,
    "income_lpa": 10.0,
    "smoker": false,
    "city": "Pune",
    "occupation": "private_job"
  }'
```

**Response:**
```json
{
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.8542,
    "class_probabilities": {
      "Low": 0.0891,
      "Medium": 0.8542,
      "High": 0.0567
    }
  }
}
```

## 🔧 Features

- **BMI Calculation**: Automatic BMI calculation from height and weight
- **Age Group Classification**: Categorizes users into age groups (young, adult, middle_aged, senior)
- **Lifestyle Risk Assessment**: Evaluates risk based on smoking habits and BMI
- **City Tier Classification**: Classifies cities into tiers (1, 2, 3) for pricing
- **Random Forest Model**: Machine learning model for accurate predictions
- **RESTful API**: Clean, documented FastAPI endpoints
- **Interactive UI**: User-friendly Streamlit interface
- **Docker Support**: Containerized deployment ready

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src
```

## 📊 Model Performance

The Random Forest model achieves high accuracy in predicting insurance premium categories based on:
- BMI (calculated from height/weight)
- Age group classification
- Lifestyle risk assessment
- City tier classification
- Income level (LPA)
- Occupation type

## 🏙️ City Tier Classification

- **Tier 1**: Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune, Ahmedabad
- **Tier 2**: Jaipur, Chandigarh, Indore, Lucknow, Patna, Ranchi, Visakhapatnam, Coimbatore, and 50+ other cities
- **Tier 3**: All other cities

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🔧 Development Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m pytest tests/`
4. Start development server: `python main.py`

## 📞 Support

For issues and questions, please create an issue in the GitHub repository.
