from urllib.parse import urljoin

import requests


ENDPOINT_URL = "https://sriram-intern-sriram-8000.demo1.truefoundry.com/predict/"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
response = requests.post(
    urljoin(ENDPOINT_URL, f'predict'),
    
    json={
            "hf_pipeline": "text-generation",
            "model_deployed_url": "https://text-gen-intern-sriram.demo1.truefoundry.com/v2/models/text-gen/infer/simple",

            "inputs": "Hello, how are you today?",
            "parameters":{"max_new_tokens": 100,
                        "temperature": 0.7,
                        "top_k": 5,
                        "top_p": 0.9,
                        "return_full_text": True},
    }

    
)

result = response.json()

print(result)
