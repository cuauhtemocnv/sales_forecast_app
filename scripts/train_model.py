# scripts/train_model.py
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import joblib
import os
import argparse
from pathlib import Path

def main():
    # Set up argument parsing for flexibility
    parser = argparse.ArgumentParser(description='Train Prophet model on Walmart sales data')
    parser.add_argument('--data-path', type=str, default='data/walmart.csv', 
                       help='Path to the input CSV file')
    parser.add_argument('--model-path', type=str, default='models/prophet_model.pkl',
                       help='Path to save the trained model')
    parser.add_argument('--make-dirs', action='store_true',
                       help='Create directories if they don\'t exist')
    
    args = parser.parse_args()
    
    # Handle directory creation
    if args.make_dirs:
        os.makedirs(os.path.dirname(args.data_path), exist_ok=True)
        os.makedirs(os.path.dirname(args.model_path), exist_ok=True)
    
    try:
        # Load dataset
        print(f"📊 Loading data from {args.data_path}...")
        df = pd.read_csv(args.data_path)
        df = df.rename(columns={"Date": "ds", "Weekly_Sales": "y"})
        
        # Convert date format
        print("🔄 Processing dates...")
        df['ds'] = pd.to_datetime(df['ds'], format='%d-%m-%Y')
        
        # Basic data validation
        print(f"📈 Dataset shape: {df.shape}")
        print(f"📅 Date range: {df['ds'].min()} to {df['ds'].max()}")
        print(f"📊 Sales range: ${df['y'].min():.2f} to ${df['y'].max():.2f}")
        
        # Fit the model
        print("🤖 Training Prophet model...")
        model = Prophet()
        model.fit(df)
        
        # Save model
        print(f"💾 Saving model to {args.model_path}...")
        joblib.dump(model, args.model_path)
        
        # Generate some basic diagnostics
        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)
        
        print("✅ Model training completed successfully!")
        print(f"📈 Forecast generated for {len(forecast)} periods")
        print(f"🔮 Final forecast date: {forecast['ds'].max()}")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: Data file not found at {args.data_path}")
        print("Please ensure the dataset exists or use --data-path to specify its location")
        return False
    except Exception as e:
        print(f"❌ Error during model training: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
