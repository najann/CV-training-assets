# CV Training Assets

>Note: The code in this repository is not maintained anymore.

This repository contains some demo applications accompanying the lectures by Björn Schmitz at the KIT.
There is a specific ReadMe for each demo in the corresponding subfolder.
Therefore, this ReadMe is targeted at providing some general insights and experience gained during the development of computer vision demos.

I concentrated on using the currently most popular libraries, namely PyTorch, Keras resp. Tensorflow and OpenCV.

## BentoML

"BentoML is an open-source framework for high-performance machine learning model serving." ([BentoML](https://docs.bentoml.org/en/latest/))
It facilitates deployment-related, preparative and operative tasks in the field of ML models.
Conveniently, BentoML even produces a Dockerfile which you can use to containerize your model and provide an easy API.

## Flask vs. Bottle vs. Pyramid

### General Structure of the demo apps

The typical functioning of the apps is as follows:

If a users comes to the landing page (`/`) the model is loaded if needed.
Once an image was chosen (and threshold/confidence set), it is send via a form POST request to the app, which reads the image data into memory and preprocesses it.
Then, the image is fed into the model.
Once the predictions are ready, they are marked in the image with rectangles and the assemblage is (optimized and) stored in the container.
The result view displays this image and by clicking on it, a user could download it.
If the user returns to the home page using the button below the image, the latter will be deleted to free up some space.
