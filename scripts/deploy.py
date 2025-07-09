#!/usr/bin/env python3
"""
Deployment script for Insurance Premium Prediction API
"""
import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    else:
        print(f"Success: {result.stdout}")
        return True

def deploy_backend():
    """Deploy the FastAPI backend"""
    print("Deploying Backend...")
    commands = [
        ("docker build -f deployment/Dockerfile.backend -t insurance-api .", "Building backend Docker image"),
        ("docker run -d -p 8000:8000 --name insurance-api-container insurance-api", "Running backend container")
    ]
    
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            return False
    return True

def deploy_frontend():
    """Deploy the Streamlit frontend"""
    print("Deploying Frontend...")
    commands = [
        ("docker build -f deployment/Dockerfile.frontend -t insurance-ui .", "Building frontend Docker image"),
        ("docker run -d -p 8501:8501 --name insurance-ui-container insurance-ui", "Running frontend container")
    ]
    
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "backend":
            deploy_backend()
        elif sys.argv[1] == "frontend":
            deploy_frontend()
        elif sys.argv[1] == "all":
            deploy_backend()
            deploy_frontend()
        else:
            print("Usage: python deploy.py [backend|frontend|all]")
    else:
        print("Usage: python deploy.py [backend|frontend|all]")
