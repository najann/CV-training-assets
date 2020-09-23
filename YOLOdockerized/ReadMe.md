# YouOnlyLookOnce Demo

## About YOLO

YOLO is a real-time object detector.
With a single neural network evaluation, the bounding boxes for objects in an image as well as the respective class + probability are calculated.

Currently, [v3](https://pjreddie.com/media/files/papers/YOLOv3.pdf) is the most often referenced and implemented version of YOLO.
However, this year, both [v4 and v5](https://towardsdatascience.com/yolo-v4-or-yolo-v5-or-pp-yolo-dad8e40f7109) have been introduced.
The main YOLO implementations are based on [Darknet](https://pjreddie.com/darknet/), an open-source neural network framework.

If you want to read more about YOLO, I can recommend the following websites:

- [YOLOv4 Article by AlexeyAB](https://medium.com/@alexeyab84/yolov4-the-most-accurate-real-time-neural-network-on-ms-coco-dataset-73adfd3602fe)

- [Darknet Usage and Training Guide](https://colab.research.google.com/drive/1_GdoqCJWXsChrOiY8sZMr_zbr_fH-0Fg?usp=sharing#scrollTo=G9Fv0wjCMPYY)

- [YOLO architecture by Lutz Roeder](https://lutzroeder.github.io/netron/?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexeyAB%2Fdarknet%2Fmaster%2Fcfg%2Fyolov4.cfg)

## YOLO Implementation

For this demo, the net [configuration](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg) and [weights](https://pjreddie.com/media/files/yolov3.weights) from [Joseph Redmon's website](https://pjreddie.com/darknet/yolo/) are used (608x608 input).
You can get them running `wget -nv -P ./yolo/cvdetect/yolo-coco https://pjreddie.com/media/files/yolov3.weights`.
These files serve as the input for openCVs `readNetFromDarknet()` [function](https://docs.opencv.org/3.4/d6/d0f/group__dnn.html#gafde362956af949cce087f3f25c6aff0d).
The latter returns the bounding box coordinates, class and confidence for all object detections.
For those detections with confidence above a given threshold, [Non-Maximum Suppression](https://towardsdatascience.com/non-maximum-suppression-nms-93ce178e177c) is performed to reduce the number of individual detections.

## Embedding YOLO In A Demo

### The `Bottle` App

This demo is implemented with the independent micro web-framework [Bottle](https://bottlepy.org/docs/dev/).
Due to its small size, it is very handy for smaller demos or PoCs, which are often also deployed with limited cloud resources.

A user can upload an image, define the confidence and NMS thresholds (or keep the defaults) and download the image with any detected objects.

### Deployment

For (almost :wink:) hassle-free development and reproduction, this demo is containerized.
The [Dockerfile](./Dockerfile) outlines the image build steps.
To get a running container, run the following commands:

```bash
docker build -t yolo-opencv .
docker run -d --name yolo-opencv -p 8080:8080 yolo-opencv
```

> To reduce the image size, the `python:3.7-slim` base image was used. However, to make OpenCV work, the missing packages `libsm6, libxext6, libxrender-dev` and `libglib2.0-0` need to be installed.

#### :white_check_mark: On Heroku

This application was finally deployed on [heroku](https://damp-hollows-09068.herokuapp.com).
Roughly, the steps for that are:

```bash
heroku login
heroku container:login
heroku create
heroku container:push web
heroku container:release web
heroku open
```

#### :no_entry: On IBM Cloud

Initially, the app was published via the [IBM Cloud Kubernetes Service](https://cloud.ibm.com/kubernetes/catalog/create).
However, the resources there are very limited and the Docker image of the app was too large for the image registry.
For the sake of completeness and reference, you can find the associated files/guides anyway:

- [init_cluster.sh](./init_cluster.sh)
- [update_cluster.sh](./update_cluster.sh)
- [yolo-docker-deployment.yaml](./yolo-docker-deployment.yaml)
- [yolo-service.yaml](./yolo-service.yaml)
