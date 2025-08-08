from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# 1. Define the FastAPI app
app = FastAPI()

# 2. Input schema using Pydantic
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 3. Load the model (adjust path if needed)
MODEL_PATH = "models/best_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

# 4. Define prediction route
@app.post("/predict")
def predict_species(input_data: IrisInput):
    try:
        data = [[
            input_data.sepal_length,
            input_data.sepal_width,
            input_data.petal_length,
            input_data.petal_width
        ]]

        # ✅ Use snake_case column names to match training
        df = pd.DataFrame(data, columns=["sepal_length", "sepal_width",
                                         "petal_length", "petal_width"])

        prediction = model.predict(df)
        species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
        return {"prediction": species_map[int(prediction[0])]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
