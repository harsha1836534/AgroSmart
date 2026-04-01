import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(os.path.join(BASE, "data", "crop_recommendation.csv"))

# Clean data
df = df.dropna()

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

pickle.dump(model, open(os.path.join(BASE, "models", "crop_model.pkl"), "wb"))

print("Crop model trained and saved!")