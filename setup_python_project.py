import os
import subprocess
import sys
import venv

# Configuration
PROJECT_NAME = "gold_token_project"
VENV_DIR = os.path.join(PROJECT_NAME, "venv")
DEPENDENCIES = ["requests", "pyjwt", "markdown2"]  # For Ghost API, GitHub, Markdown
DIRECTORIES = ["scripts", "config", "data"]  # Subfolders
REQUIREMENTS_FILE = os.path.join(PROJECT_NAME, "requirements.txt")
MAIN_SCRIPT = os.path.join(PROJECT_NAME, "scripts", "main.py")
GITIGNORE_FILE = os.path.join(PROJECT_NAME, ".gitignore")

# Create project directory and subdirectories
def create_project_structure():
    if not os.path.exists(PROJECT_NAME):
        os.makedirs(PROJECT_NAME)
        print(f"Created project directory: {PROJECT_NAME}")
    else:
        print(f"Project directory already exists: {PROJECT_NAME}")

    for directory in DIRECTORIES:
        dir_path = os.path.join(PROJECT_NAME, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {dir_path}")

# Setup virtual environment
def setup_venv():
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in {VENV_DIR}...")
        venv.create(VENV_DIR, with_pip=True)
        print("Virtual environment created.")
    else:
        print(f"Virtual environment already exists in {VENV_DIR}")

    # Get pip path
    is_windows = sys.platform.startswith("win")
    pip_path = os.path.join(VENV_DIR, "Scripts" if is_windows else "bin", "pip")

    # Create requirements.txt
    with open(REQUIREMENTS_FILE, "w") as f:
        f.write("\n".join(DEPENDENCIES))
        print(f"Created {REQUIREMENTS_FILE}")

    # Install dependencies
    print("Installing dependencies...")
    subprocess.check_call([pip_path, "install", "-r", REQUIREMENTS_FILE])
    print("Dependencies installed.")

# Create placeholder main.py
def create_main_script():
    main_content = """\
# main.py
# Placeholder script for Gold Token Project

def main():
    print("Welcome to the Gold Token Project!")
    # Add your code here (e.g., fetch from https://github.com/broward/token/ or publish to https://broward.ghost.io/)

if __name__ == "__main__":
    main()
"""
    if not os.path.exists(MAIN_SCRIPT):
        with open(MAIN_SCRIPT, "w") as f:
            f.write(main_content)
            print(f"Created placeholder script: {MAIN_SCRIPT}")

# Create .gitignore
def create_gitignore():
    gitignore_content = """\
venv/
__pycache__/
*.pyc
config/
"""
    if not os.path.exists(GITIGNORE_FILE):
        with open(GITIGNORE_FILE, "w") as f:
            f.write(gitignore_content)
            print(f"Created {GITIGNORE_FILE}")

# Main
def main():
    print(f"Setting up Python project: {PROJECT_NAME}")
    create_project_structure()
    setup_venv()
    create_main_script()
    create_gitignore()
    print(f"\nProject setup complete! To activate the virtual environment:")
    if sys.platform.startswith("win"):
        print(f"  cd {PROJECT_NAME}")
        print(f"  venv\\Scripts\\activate")
    else:
        print(f"  cd {PROJECT_NAME}")
        print(f"  source venv/bin/activate")
    print(f"Then run scripts from the 'scripts' folder, e.g.:")
    print(f"  python scripts/main.py")
    print(f"\nNext steps:")
    print(f"  - Add scripts to 'scripts/' (e.g., for Ghost API or GitHub).")
    print(f"  - Store API keys in 'config/' (excluded by .gitignore).")
    print(f"  - Save JSON schemas or data in 'data/'.")

if __name__ == "__main__":
    main()
        









