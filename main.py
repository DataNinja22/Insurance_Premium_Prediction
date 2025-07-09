#!/usr/bin/env python3
"""
Main entry point for the Insurance Premium Prediction Application
"""
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

if __name__ == "__main__":
    import uvicorn
    from src.api.main import app
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
