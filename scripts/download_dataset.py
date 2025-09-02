import os
import zipfile
import subprocess
import shutil

# Paths
DATA_DIR = "data"
ZIP_PATH = os.path.expanduser("~/Downloads/walmart-dataset.zip")
CSV_NAME = "Walmart.csv"
DEST_PATH = os.path.join(DATA_DIR, "walmart.csv")

os.makedirs(DATA_DIR, exist_ok=True)

# Step 1: Download the dataset with curl (requires Kaggle API logged in)
print("Downloading Walmart dataset...")
subprocess.run([
    "curl", "-L", "-o", ZIP_PATH,
    "https://www.kaggle.com/api/v1/datasets/download/yasserh/walmart-dataset"
], check=True)

# Step 2: Extract the Walmart.csv file
print("Extracting CSV from zip...")
with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
    # Look for Walmart.csv inside the zip
    for file in zip_ref.namelist():
        if file.endswith("Walmart.csv"):
            zip_ref.extract(file, DATA_DIR)
            # Move/rename to data/walmart.csv
            extracted_path = os.path.join(DATA_DIR, file)
            shutil.move(extracted_path, DEST_PATH)
            print(f"{CSV_NAME} saved to {DEST_PATH}")
            break
    else:
        raise FileNotFoundError("Walmart.csv not found inside the zip!")

print("✅ Dataset ready.")
