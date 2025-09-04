import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import joblib

# Load dataset
df = pd.read_csv("../data/walmart.csv")
df = df.rename(columns={"Date": "ds", "Weekly_Sales": "y"})

# FIX: Use correct date format (day-month-year)
df['ds'] = pd.to_datetime(df['ds'], format='%d-%m-%Y')
import os
from prophet import Prophet
import joblib

# Create the models directory if it doesn't exist
models_dir = "../models"
os.makedirs(models_dir, exist_ok=True)

# Fit the model
model = Prophet()
model.fit(df)

# Save model
joblib.dump(model, "../models/prophet_model.pkl")
print("✅ Model saved to ../models/prophet_model.pkl")
