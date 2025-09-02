from fastapi import FastAPI
import joblib
import pandas as pd


app = FastAPI()
model = joblib.load("models/prophet_model.pkl")


@app.get("/forecast")
def get_forecast(days: int = 30):
  future = model.make_future_dataframe(periods=days)
  forecast = model.predict(future)
  return forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(days).to_dict(orient="records")
