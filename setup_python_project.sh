#!/bin/bash

# Script to set up a standard Python project structure

# Project name (can be passed as an argument, default to "my_python_project")
PROJECT_NAME=${1:-my_python_project}

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it first (e.g., sudo apt install python3)."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing it now..."
    sudo apt update
    sudo apt install -y python3-pip
fi

# Check if virtualenv is installed, install if missing
if ! pip3 show virtualenv &> /dev/null; then
    echo "virtualenv is not installed. Installing it now..."
    pip3 install virtualenv
fi

# Create the project directory
echo "Creating project directory: $PROJECT_NAME"
mkdir $PROJECT_NAME
cd $PROJECT_NAME

# Create the directory structure
mkdir -p src/my_project
mkdir tests
mkdir docs

# Create a virtual environment
echo "Setting up virtual environment..."
python3 -m virtualenv venv

# Activate the virtual environment
source venv/bin/activate

# Install some basic dependencies (pytest for testing)
echo "Installing pytest..."
pip install pytest

# Create initial files
# .gitignore
cat <<EOL > .gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
venv/
*.egg-info/
dist/
build/
*.egg

# IDEs
.idea/
.vscode/

# Misc
*.log
*.pot
*.pyc
.DS_Store
EOL

# README.md
cat <<EOL > README.md
# $PROJECT_NAME

A standard Python project setup.

## Getting Started

1. Clone this repository.
2. Activate the virtual environment: \`source venv/bin/activate\`
3. Install dependencies: \`pip install -r requirements.txt\`
4. Run tests: \`pytest\`

## Project Structure

- \`src/\`: Source code for the project.
- \`tests/\`: Unit tests.
- \`docs/\`: Documentation.
- \`venv/\`: Virtual environment.
EOL

# requirements.txt
cat <<EOL > requirements.txt
pytest
EOL

# setup.py
cat <<EOL > setup.py
from setuptools import setup, find_packages

setup(
    name="$PROJECT_NAME",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A standard Python project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
EOL

# src/my_project/__init__.py
touch src/my_project/__init__.py

# src/my_project/main.py
cat <<EOL > src/my_project/main.py
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    print(hello_world())
EOL

# tests/__init__.py
touch tests/__init__.py

# tests/test_main.py
cat <<EOL > tests/test_main.py
from my_project.main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"
EOL

# Deactivate the virtual environment
deactivate

#post-install instructions
python3.9 -m pip install --upgrade pip


# Print completion message
echo "Python project '$PROJECT_NAME' has been set up successfully!"
echo "To get started:"
echo "  cd $PROJECT_NAME"
echo "  source venv/bin/activate"
echo "  pip install -r requirements.txt"
echo "  pytest"
