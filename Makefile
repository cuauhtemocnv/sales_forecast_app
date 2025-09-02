install:
pip install -r requirements.txt


download:
python scripts/download_dataset.py


train:
jupyter nbconvert --to notebook --execute notebooks/eda_modeling.ipynb --inplace


dashboard:
streamlit run app/dashboard.py


api:
uvicorn api.main:app --reload


docker-build:
docker build -t sales-api ./docker


docker-run:
docker run -p 8000:8000 sales-api
