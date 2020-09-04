# PyTorch Transfer Learning Demo

_Note:_ This app was deployed on heroku and can be found [here](http://sheltered-mountain-05928.herokuapp.com)

## Flask WebApp

For this demo, I used the classic Python micro web-framework Flask.
It uses Jinja2 for HTML-templating, too.
However, this time the input image is not processed by the web app itself.
Instead, the app makes an HTTP request to another container (heroku dyno/app) providing the API endpoint for an encapsulated model prediciton (see `/analyze` in [\_\_init\_\_.py](./__init.py__)).

Again, the web app is constructed as a package so that a simple `pip install .` will take care of the correct setup (dependencies, etc.).

## :sparkles: Model Serving With BentoML

With this demo, you'll also get to know a very handy method to make your ML model available independent from the web application's route.
This is important if you're working with a microservice-architecture.
With BentoML you have an easy-to-handle library at hand to serve your model independently.
[bento_service.py](./bento_service.py) contains a class, which wraps your model.
It takes an image as input, preprocesses it, forwards it to the model and returns any output predictions.

To make your model ready for being served, run `python use_bentoml.py`.
This will load the model you fine-tuned using the [Jupyter Notebook for TL with PyTorch](../TransferLearningPytorch.ipynb).
It is packed into the classifier class and saved as a service.

```bash
bentoml serve /Path/to/bentoml/repository/AntOrBeeClassifier/id
```

The command above can be used to serve the model locally.
Alternatively, BentoML also creates a Dockerfile, which you can use out-of-the-box to deploy the model service to your platform of choice, e.g. heroku.
From within `/Path/to/bentoml/repository/AntOrBeeClassifier/id`:

```bash
heroku create
heroku container:push web
heroku container:release web
```

> Attention: Don't try to put the classifier class and `main()` into the same file. This will break the creation of you service (see [this section in the documentation](https://docs.bentoml.org/en/latest/concepts.html#creating-bentoservice))

This will create a heroku app only for the TL model.
Once your dyno is ready, insert the service's URL in line 10 of [\_\_init\_\_.py](./__init.py__) and continue with the [deployment of your web app](#deployment-using-the-makefile).

## Deployment Using The Makefile

This demo lets you benefit from a [Makefile](./Makefile) to cope with the Flask Docker deployment.
Simply run `make build`, `make run`, `make kill` or `make herokup` to build your Docker image, [run](localhost:5000) a container locally, kill it or deploy it as a Heroku app (no need to create the app beforehand).

### :whale: The Dockerfile

For local development, you need to uncomment some lines in the [Dockerfile](./Dockerfile), so that your container is accessible.
In addition, you should not use Flask's development server on heroku which is why you need a more reliable WSGI-server (e.g. gunicorn).

The chosen Docker image is alpine-based.
As it is missing some packages to be able to install `numpy`, these are added "manually".
