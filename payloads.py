
def payloads(pipeline):
    if pipeline == "text-generation":

        payload_text_generation = {
            "inputs": "Hello, how are you today?",
            "parameters": {
                    "max_new_tokens": 100,
                    "temperature": 0.7,
                    "top_k": 5,
                    "top_p": 0.9,
                    "return_full_text": True
                }
        }

        return payload_text_generation


    if pipeline == "object-generation":

        payload_obj_detection = {
            "id": "string",
            "parameters": {
                "content_type": "string",
                "headers": {}
            },
            "inputs": [
                {
                    "name": "string",
                    "shape": [0],
                    "datatype": "BOOL",
                    "parameters": {
                        "content_type": "string",
                        "headers": {}
                    },
                    "data": None
                }
            ],
            "outputs": [
                {
                    "name": "string",
                    "parameters": {
                        "content_type": "string",
                        "headers": {}
                    }
                }
            ]
        }
        
        return payload_obj_detection


