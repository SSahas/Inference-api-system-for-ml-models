
def payloads(pipeline):
    if pipeline == "text-generation":

        payload_text_generation = {
            "parameters": {"content_type": "str"},
            "inputs": [
                {
                    "name": "array_inputs",
                    "shape": [1],
                    "datatype": "BYTES",
                    "data": ["What is alpaca? How is it different from a llama?"]
                },
                {
                    "name": "max_new_tokens",
                    "shape": [-1],
                    "datatype": "BYTES",
                    "data": ["20"],
                    "parameters": {"content_type": "hg_json"}
                }
            ]
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


