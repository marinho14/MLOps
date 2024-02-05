import joblib
import sklearn
from fastapi import FastAPI, HTTPException , APIRouter
import json 
import uvicorn
from pydantic import BaseModel

class Penguin(BaseModel):
    culmenLen: float
    culmenDepth: float
    flipperLen: int
    bodyMass: int
    sex: str
    delta15N: float
    delta13C: float

app = FastAPI()
    
def decode_input(self , input_json: json):
    
    self.input_df = input_json
    return True
    
def predict(self , model):
    
    inference = 1
    return inference

@app.post("/predict/{model_name}")
def predict_model(model_name: str, input_data : Penguin):
    # Cargar el modelo según el nombre proporcionado
    model_path = f"models/{model_name}.pkl"
    model = joblib.load(model_path)

    # Decodificar los datos de entrada
    # decoded_input = decode_input(input_data)

    # Realizar predicción
    # prediction = predict(decoded_input, model)
    return {"model_used": model_name, "prediction": [1]}

if __name__ == "__main__":
    # Ejecutar la aplicación con Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)