The Aim of this project is to improve the user experience , the ml models are deployed in cloud using seldons ml server and the parameters to call the model for predictions are complex and not userfriendly. so in this project i have tried to improve the user experience and tried to build a system which works like huggingface inference api system.


# tf_deploy

- > main.py is the fastapi file and payloads is another file which contain the parameters to call the different models deployed on truefoundry

- > Run the inference.py file, with this code we can send inputs for the models locally from our pc  and it gets the output just like huggingface inference api system.

- > Wrote fastapi service for three different pipelines "text-generation", "token-classification", "zero-shot-clssification".
