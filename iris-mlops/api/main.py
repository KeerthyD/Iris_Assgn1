from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os
from utils.logger import init_db, log_prediction
from pydantic import BaseModel, Field
from prometheus_fastapi_instrumentator import Instrumentator

# 1. Define the FastAPI app
app = FastAPI()
Instrumentator().instrument(app).expose(app)


# 2. Input schema using Pydantic
class IrisInput(BaseModel):
    sepal_length: float = Field(..., ge=4.0, le=8.0)
    sepal_width: float = Field(..., ge=2.0, le=5.0)
    petal_length: float = Field(..., ge=1.0, le=7.0)
    petal_width: float = Field(..., ge=0.1, le=3.0)


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

        df = pd.DataFrame(data, columns=["sepal_length", "sepal_width",
                                         "petal_length", "petal_width"])

        prediction = model.predict(df)
        species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
        predicted_species = species_map[int(prediction[0])]
        log_prediction(input_data.dict(), predicted_species)
        return {"prediction": predicted_species}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.on_event("startup")
def startup_event():
    init_db()
