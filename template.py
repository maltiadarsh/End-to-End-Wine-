import os  # For interacting with the operating system (creating directories, checking file existence, etc.)
from pathlib import Path  # For handling file paths in a platform-independent way
import logging  # For logging messages to track script execution
# Setting up logging to display timestamps and informative messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
# Define the project name to organize files under a specific namespace
project_name = "mlProject"


# List of all files and their paths that need to be created
list_Of_files = [
    f"src/{project_name}/__init__.py",  
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",  
    f"src/{project_name}/config/__init__.py",  
    f"src/{project_name}/config/configuration.py",  
    f"src/{project_name}/pipeline/__init__.py",  
    f"src/{project_name}/entity/__init__.py",  
    f"src/{project_name}/entity/config_entity.py",  
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml", 
    "params.yaml",  
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    "test.py"

]


# Iterate over each file path in the list
for filepath in list_Of_files:
    filepath = Path(filepath)  # Convert to a Path object for easier handling
    filedir, filename = os.path.split(filepath)  # Split into directory and file name

    # Create the directory if it doesn't already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # `exist_ok=True` prevents errors if the directory exists
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        # Log that the file already exists
        logging.info(f"{filename} already exists")
