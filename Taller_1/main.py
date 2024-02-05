import joblib
import sklearn
from fastapi import FastAPI
import json 

class PenguinsApi():
    
    # Constructor (__init__)
    def __init__(self, pr_model, sc_model):
        self.app = FastAPI()

        self.pr_model = joblib.load(pr_model)
        self.sc_model = joblib.load(sc_model)
    
    def decode_imput(self , input_json: json):
        
        self.input_df = input_json
        return True
        
    def predict(self, input: json , model):
        
        inference = 1
        return inference

    
        
        