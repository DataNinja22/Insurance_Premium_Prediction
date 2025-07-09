# Multi-stage Dockerfile for Insurance Premium Prediction App

# Stage 1: Backend (FastAPI)
FROM python:3.11-slim as backend

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY data/ ./data/

# Expose port
EXPOSE 8000

# Command to run the backend
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Stage 2: Frontend (Streamlit)
FROM python:3.11-slim as frontend

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy UI code
COPY ui/ ./ui/

# Expose port
EXPOSE 8501

# Command to run the frontend
CMD ["streamlit", "run", "ui/ui.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Stage 3: Development (Full setup)
FROM python:3.11-slim as development

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose both ports
EXPOSE 8000 8501

# Default command for development
CMD ["bash"]
