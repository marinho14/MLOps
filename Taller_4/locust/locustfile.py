from locust import HttpUser, task, constant
from pydantic import BaseModel
import json
import requests

def ping_host(host_url):
    try:
        response = requests.get(host_url)
        if response.status_code == 200:
            print(f"Ping exitoso a {host_url}")
        else:
            print(f"No se pudo conectar a {host_url}. Estado de respuesta: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error al conectar con {host_url}: {e}")

class LoadTest(HttpUser):
    wait_time = constant(1)
    host = "http://fastapi:8000/"

    @task
    def predict(self):
        #ping_host(self.fastapihost)
        request_body = {
            "Elevation": [0],
            "Aspect": [0],
            "Slope": [0],
            "Horizontal_Distance_To_Hydrology": [0],
            "Vertical_Distance_To_Hydrology": [0],
            "Horizontal_Distance_To_Roadways": [0],
            "Hillshade_9am": [0],
            "Hillshade_Noon": [0],
            "Hillshade_3pm": [0],
            "Horizontal_Distance_To_Fire_Points": [0],
            "Wilderness_Area": ["Rawah"],
            "Soil_Type": ["C7745"],
            "Cover_Type": [0]
        }

        headers = {
            "Content-Type": "application/json",
        }

        response = self.client.post(
            "/predict/modelo_base", json=request_body, headers=headers
        )

        # print(f"Response status code: {response.status_code}")
        # print(f"Response content: {response.content.decode('utf-8')}")
