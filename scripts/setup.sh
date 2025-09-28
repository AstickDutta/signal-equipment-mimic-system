#!/bin/bash

# Setup script for Signal Equipment API

echo "Setting up Signal Equipment API development environment..."


if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3.8 or higher."
    exit 1
fi


if ! command -v docker &> /dev/null; then
    echo "Docker is required but not installed. Please install Docker."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is required but not installed. Please install Docker Compose."
    exit 1
fi


if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi


echo "Activating virtual environment..."
source .venv/bin/activate


echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt


echo "Running tests..."
pytest tests/ -v

echo "Setup complete! You can now run:"
echo "  make docker-run    # Run with Docker"
echo "  make dev          # Run development server"
echo "  make test         # Run tests"