import joblib
import sklearn
from fastapi import FastAPI, HTTPException , APIRouter
import uvicorn
from pydantic import BaseModel
from typing import List
import pandas as pd

class Penguin(BaseModel):
    culmenLen: List[float]
    culmenDepth: List[float]
    flipperLen: List[int]
    bodyMass: List[int]
    sex: List[str]
    delta15N: List[float]
    delta13C: List[float]

species_mapping = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}

app = FastAPI()
    
def decode_input(input):
    input_dict=dict(input)
    df = pd.DataFrame.from_dict(input_dict)
    df['sex'] = df['sex'].apply(lambda x: 0 if x == 'Male' else 1)
    return df
    

@app.post("/predict/{model_name}")
def predict_model(model_name: str, input_data : Penguin):
    # Cargar el modelo según el nombre proporcionado
    model_path = f"models/{model_name}.pkl"
    model = joblib.load(model_path)

    # Decodificar los datos de entrada
    decoded_input = decode_input(input_data)
    prediction = model.predict(decoded_input)
    prediction_list = prediction.tolist()
    prediction_mapped = [list(species_mapping.keys())[list(species_mapping.values()).index(x)] for x in prediction_list]
    
    return {"model_used": model_name, "prediction":prediction_mapped}

# if __name__ == "__main__":
#     # Ejecutar la aplicación con Uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)