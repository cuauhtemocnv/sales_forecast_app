import pandas as pd
import os


URL = "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv" # placeholder
# Replace with Walmart dataset mirror if available


os.makedirs("data", exist_ok=True)


print("Downloading dataset...")
df = pd.read_csv(URL)
df.to_csv("data/walmart.csv", index=False)
print("Dataset saved to data/walmart.csv")
