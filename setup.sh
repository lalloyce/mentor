#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
pip install django djangorestframework pillow mysql-connector-python

# Make and apply migrations
echo "Making migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate

# Run the seeder
echo "Running database seeder..."
python manage.py seed_data

echo "Setup complete! You can now run 'python manage.py runserver' to start the development server."
