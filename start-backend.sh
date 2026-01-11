#!/bin/bash

echo "Starting Wiki Quiz Backend Server..."
cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

if [ ! -f ".env" ]; then
    echo ""
    echo "WARNING: .env file not found!"
    echo "Please create backend/.env file with:"
    echo "  GEMINI_API_KEY=your_api_key_here"
    echo ""
    echo "You can copy backend/.env.example to backend/.env and edit it."
    echo ""
    read -p "Press enter to continue anyway..."
fi

echo "Installing/updating dependencies..."
pip install -r requirements.txt --quiet

echo ""
echo "Starting FastAPI server on http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo ""
python run.py

