import streamlit as st
import pandas as pd
import joblib
from prophet.plot import plot_plotly


st.title("📈 Retail Sales Forecast Dashboard")


# Load model
model = joblib.load("models/prophet_model.pkl")


# Load dataset
df = pd.read_csv("data/walmart.csv")
df = df.rename(columns={"Date": "ds", "Weekly_Sales": "y"})


# Forecast
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)


st.write("### Forecast Plot")
st.plotly_chart(plot_plotly(model, forecast))
