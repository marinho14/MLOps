from locust import HttpUser, task, constant
from pydantic import BaseModel
import json

class CoverType(BaseModel):
    Elevation: float = 3154
    Aspect: float = 351
    Slope: float = 13
    Horizontal_Distance_To_Hydrology: float = 658
    Vertical_Distance_To_Hydrology: float = 191
    Horizontal_Distance_To_Roadways: float = 6164
    Hillshade_9am: float = 172
    Hillshade_Noon: float = 233
    Hillshade_3pm: float = 200
    Horizontal_Distance_To_Fire_Points: float = 1473
    Wilderness_Area: str = "Rawah"
    Soil_Type: str = "C7746"
    Cover_Type: float = 0

class LoadTest(HttpUser):
    wait_time = constant(1)
    host = "http://localhost:8000"

    @task
    def predict(self):
        request_body = json.dumps(CoverType().dict())
        headers = {
            "Content-Type": "application/json",
        }
        self.client.post(
            "/predict/modelo_base", data=request_body, headers=headers
        )
