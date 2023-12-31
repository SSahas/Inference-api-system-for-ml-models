import requests
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from typing import Dict, Any
from payloads import payloads
import os

app = FastAPI(root_path=os.getenv("TFY_SERVICE_ROOT_PATH"))


class PredictRequest(BaseModel):
    hf_pipeline:  str
    model_deployed_url: str
    inputs: str 
    parameters: Dict[str, Any]


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}


@app.post(path="/predict")
async def text_generation(request: PredictRequest):
    if request.hf_pipeline == "text-generation":
    

        payload = payloads(request.hf_pipeline)

        payload["inputs"] = request.inputs

        response = requests.post(
            request.model_deployed_url,
            json=payload,
            headers=headers
        )
        result = response.json()
        return result
    
    elif request.hf_pipeline == "zero-shot-classification":

        payload = payload(request.hf_pipeline)
        payload["inputs"] = request.inputs
        payload["parameters"]["candidate_labels"] = request.parameters["parameters"]["candidate_labels"]

        response = requests.post(
            request.model_deployed_url,
            json=payload,
            headers=headers
        )
        result = response.json()
        return result

    elif request.hf_pipeline == "token-classification":

        payload = payload(request.hf_pipeline)
        payload["inputs"][0]["data"] = request.inputs

        response = requests.post(
            request.model_deployed_url,
            json=payload,
            headers=headers
        )
        result = response.json()
        return result
    else:

        return ValueError("invalid payload inputs") 




    
    



        
