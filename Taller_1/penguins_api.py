import joblib
import sklearn
from fastapi import FastAPI, HTTPException , APIRouter
import uvicorn
from pydantic import BaseModel
from typing import List
import pandas as pd
import os

class Penguin(BaseModel):
    studyName: List[str] = ['PAL0708']
    sampleNumber: List[int] = [1]
    region: List[str] = ['Anvers']
    island: List[str] = ['Torgersen']
    stage: List[str] = ['Adult, 1 Egg Stage']
    individualID: List[str] = ['N1A1']
    clutchCompletion: List[str] = ['Yes']
    dateEgg: List[str] = ['11/11/07']
    culmenLen: List[float] = [39.1]
    culmenDepth: List[float] = [18.7]
    flipperLen: List[int] = [181]
    bodyMass: List[int] = [3750]
    sex: List[str] = ['MALE']
    delta15N: List[float] = [0.0]
    delta13C: List[float] = [0.0]
    comments: List[str] = ['Not enough blood for isotopes.'] 

species_mapping = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}

app = FastAPI()
    
def decode_input(input):
    input_dict=dict(input)
    df = pd.DataFrame.from_dict(input_dict)
<<<<<<< HEAD
    df['sex'] = sex_label_encoder.transform(df['sex'])
=======
    df['sex'] = df['sex'].apply(lambda x: 0 if x == 'MALE' else 1)
>>>>>>> parent of b246146 (Update README.md)
    model_columns = ['culmenLen', 'culmenDepth', 'flipperLen', 'bodyMass', 'sex', 'delta15N', 'delta13C']
    df = df[model_columns]
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

@app.get("/get_models")
def get_models():
    dir_list = os.listdir("models")
    models_avaible = [elemento.split(".")[0] for elemento in dir_list]
    return models_avaible
    
# if __name__ == "__main__":
#     # Ejecutar la aplicación con Uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)