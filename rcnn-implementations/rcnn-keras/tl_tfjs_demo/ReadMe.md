# TensorflowJS Demo

This subdirectory contains the code for a tfjs demo consisting of two containers.
A deployed version (IBM Cloud Kubernetes Service) can be found [here](http://173.193.68.8:31323/).

The advantage of TensorflowJS is that the inference is done "at the edge", i.e. on the client's device.
This _can_ save time if ...

1. cloud computing resources are limited
1. you expect many model calls by the same client
1. you let the client cache the model (for 20 days in this [demo](./fastapi_model/main.py)).

... because, even though it may take quite some time to download the 77MB model, this time is offset after a handful of classifications done locally instead of waiting for the image data to be transferred to the cloud, processed on limited resources and sent back.

## Model Serving with FastAPI

For the model data provision, I used [FastAPI](https://fastapi.tiangolo.com).
It's another Python web framework.
However, its intention is not to be an entire web application kit but it concentrates on APIs.
See [this](./fastapi_model/ReadMe.md) ReadMe for a more detailed explanation.

## :new: The NodeJs Web App

Unlike others, the centerpiece of this demo is a single-page nodeJS application.
It uses [Express](http://expressjs.com) as the web-framework of choice.
The only route returns [home.html](./home.html) displaying either a form to upload and image, the classification result or loading animations ([pure css](https://loading.io/css/)).
As the image is only classified in its entirety, there is no sense in downloading the result.
As a consequence, this web app does without saving the image as a file but manipulates the image elements `src` attribute as needed.
At the end of the file, the `model.json` script, which fetches the model and computes the classification, is loaded.

## Local Operation

For testing purposes, you can start both applications (Express and FastAPI) at once running `[docker-compose](./docker-compose.yml) up --build`.
This will build the images and run them in two containers within the same network thereafter.

## Deployment to IBM Cloud Kubernetes Service

In light of [above](#tensorflowjs-demo) considerations, the IBM Cloud Kubernetes Service seems to be an appropriate platform for the deployment of this demo despite its restricted resources which made it unbearable for other CV demos.

The following scripts can be invoked to (re-)deploy both apps to a Kubernetes cluster and push the corresponding images to the registry:

- [renew_api.sh](./renew_api.sh)
- [renew_web.sh](./renew_web.sh)

They make use of the following `yaml`-definitions for deployment and service.

- [api-deployment.yaml](./api-deployment.yaml)
- [api-service.yaml](./api-service.yaml)
- [web-deployment.yaml](./web-deployment.yaml)
- [web-service.yaml](./web-service.yaml)

> Note: you may be tempted to use [Kompose](https://kompose.io) to make yous `docker-compose` setup k8s-compatible. However, for me this did not work with the IBM Cloud Service due to apiVersion and label/selector conflicts which is why I recommend to create the definition files manually, resp. use above ones.
