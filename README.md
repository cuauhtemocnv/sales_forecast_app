# 📈 Retail Sales Forecasting App

An end-to-end **Retail Sales Forecasting** project using Python, Prophet, Streamlit, FastAPI, and Docker. The goal is to forecast retail sales (using the Walmart dataset) and showcase a complete data science pipeline from **data collection → model training → dashboard → API → containerized deployment**.

---

## 🚀 Features
- **Dataset Downloader**: Auto-download Walmart dataset via script (`scripts/download_dataset.py`).
- **Model Training**: Prophet model for sales forecasting (`notebooks/eda_modeling.ipynb`).
- **Dashboard**: Interactive Streamlit app with forecast visualizations (`app/dashboard.py`).
- **API**: FastAPI microservice exposing forecast endpoint (`api/main.py`).
- **Docker**: Containerized API for easy deployment (`docker/Dockerfile`).
- **Cloud Ready**: Deployable on AWS/GCP/Azure.

---

## 📂 Project Structure
```
sales_forecast_app/
├── notebooks/              # Jupyter notebooks
│   └── eda_modeling.ipynb
├── app/                    # Streamlit dashboard
│   └── dashboard.py
├── api/                    # FastAPI microservice
│   └── main.py
├── docker/                 # Docker configs
│   └── Dockerfile
├── scripts/                # Utility scripts
│   └── download_dataset.py
├── data/                   # Data (auto-created)
├── models/                 # Trained models (auto-created)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🔽 1. Setup & Install
```bash
# Clone repo
 git clone https://github.com/cuauhtemocnv/sales_forecast_app
 cd sales_forecast_app

# Create virtual environment (optional)
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 📊 2. Download Dataset
```bash
python scripts/download_dataset.py
```
This saves the Walmart dataset to `data/walmart.csv`.

---

## 🤖 3. Train Model
Open the Jupyter notebook and run training:
```bash
jupyter notebook notebooks/eda_modeling.ipynb
```
This generates `models/prophet_model.pkl`.

---

## 🖥️ 4. Run Dashboard
```bash
streamlit run app/dashboard.py
```
Go to 👉 [http://localhost:8501](http://localhost:8501) to view the dashboard.

---

## ⚡ 5. Run API
```bash
uvicorn api.main:app --reload
```
Visit 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test endpoints.

Example:
```bash
curl "http://127.0.0.1:8000/forecast?days=30"
```

---

## 🐳 6. Run with Docker
```bash
# Build image
docker build -t sales-api ./docker

# Run container
docker run -p 8000:8000 sales-api
```
Now the API is available at `http://localhost:8000/forecast`.

---

## 📦 Tech Stack
- **Python** (Pandas, Prophet, Scikit-learn basics)
- **Streamlit** (dashboard)
- **FastAPI** (REST API)
- **Docker** (containerization)
- **Plotly** (visualizations)
- **AWS/GCP/Azure ready** (deploy API & dashboard)

---

## 💡 Next Steps
- Add **LSTM/GRU models** for advanced forecasting.
- Integrate **AWS S3 + Glue** for automated data ingestion.
- Add **CI/CD with GitHub Actions**.
- Deploy on **Streamlit Cloud** (dashboard) + **AWS ECS/Lambda** (API).

---

## 🙌 Author
This project is a project included in portfolio 
