# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model and class names from file
data = joblib.load("model.joblib")
model = data["model"]
class_names = list(data["target_names"])

# Define the expected request body using Pydantic
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI(title="Iris ML API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris prediction API. Use /predict for inference."}

@app.post("/predict")
def predict_species(features: IrisFeatures):
    # Convert input features to numpy array for the model
    X_new = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    pred = model.predict(X_new)[0]  # get the predicted class index (0, 1, or 2)
    species_name = class_names[int(pred)]
    return {"prediction": species_name}
