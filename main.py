import requests
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from typing import Dict, Any
from payloads import payloads

app = FastAPI()


class PredictRequest(BaseModel):
    hf_pipeline:  str
    model_deployed_url: str
    inputs: Dict[str, Any]
    parameters: Dict[str, Any]

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}


@app.post(path="/predict")
async def text_generation(request: PredictRequest, hf_pipeline: str, model_deployed_url: str, 
                              inputs: str, parameters: Dict[str, Any]  ):
    
    payload = payloads(hf_pipeline)

    payload["inputs"][0]["data"] = inputs

    response = requests.post(
        model_deployed_url,
        json=payload,
        headers=headers
    )
    result = response.json()
    return result

