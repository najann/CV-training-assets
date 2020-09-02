# FasterRCNN demo

This subdirectory contains a demo wrapped around the PyTorchs [FasterRCNN module](https://pytorch.org/docs/stable/torchvision/models.html?highlight=fasterrcnn_resnet50_fp#faster-r-cnn).
To understand it in detail, check out the corresponding [Notebook](../FasterRCNNPytorch.ipynb) and [ReadMe](../ReadMe.md).
This ReadMe focusses on the app.

## WebApp

### Packaging

Unlike other demos in this repo, this app is constructed as a package.
Thanks to `setup.py`and the `ini`-files, you can run `pip install .` and the app with all its dependencies is properly set up.

### Pyramid Framework

This demo is implemented using the [Pyramid web framework](https://trypyramid.com).
It uses Jinja2 as the template engine for HTML files.

## Deployment

As the YOLO demo, this app contains files for both heroku and IBM Cloud Kubernetes deployment even though the final version runs on heroku, again.

### :warning: ~~On Heroku~~

For this demo, the [heroku deployment](https://rocky-caverns-97441.herokuapp.com) is git-based.
However, this only works if the code of the `rcnn_docker` directory is tracked by git separately (i.e. not as part of the CV-training-assets repository).
So, provided that your code is independently tracked by git, run:

```bash
heroku create
heroku git:remote -a <app-name>
git add .
git commit -m "..."
git push heroku master
```

Heroku will check for a Procfile and, for each process type, it starts a dyno, which runs the specified command.
In our case, a web process will be used to run the app.
The entry commands are bundled in a [run-file](./run).
For example, the necessary libraries are installed.
To save resources, `torch(vision)` is only installed as the cpu-version.
Besides, the model's checkpoint is copied to the right directory, to prevent that it's downloaded every time a user accesses the app.
Finally, the web app itself is [packaged](https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/package.html) and built.
Unfortunately, often, the previous steps take more than 60s.
As a consequence, you'll get a boot timeout which prevents you from deploying your app

### :no_entry: On IBM Cloud

Again, you'll find all necessary files for a deployment on [IBM Cloud Kubernetes Service](https://cloud.ibm.com/kubernetes/catalog/create).

- [init_cluster.sh](./init_cluster.sh)
- [update_cluster.sh](./update_cluster.sh)
- [simple-rcnn-deployment.yaml](./simple-rcnn-deployment.yaml)
- [simple-rcnn-service.yaml](./simple-rcnn-service.yaml)

Simply run:

```bash
sudo chmod +x init_cluster.sh
./init_cluster.sh
```

### :white_check_mark: Google Cloud Platform

As you can see, there is also a Dockerfile, which you'll need to deploy the FasterRCNN demo on Google Cloud Platform.
After creating a new Google Cloud project and installing the gcloud CLI (walk through gcloud init, too :wink:) , build the Docker image:

```bash
docker build -t eu.gcr.io/<PROJECT_ID>/rcnn-simple
```

Then, push the image:

```bash
gcloud auth configure-docker
docker push gcr.io/<PROJECT_ID>/rcnn-simple
```

From the Google Kubernetes Engine Workloads menu in the Google Cloud Console, click _Deploy_ and choose _Existing Container Image_.
Select the image you just pushed to Container Registry and click _Deploy_.
[This tutorial](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app#console_1) explains the steps in more detail.

_Note:_ The app's cluster on Google Cloud Platform is no longer available.
Even though first-time users have a free credit of about 250€, this is depleted faster than you might expect.
If you enable auto-scaling or manually increase the number of replicas, you'll quickly get billed for quite a few EC2 instances (=> summing up to more than half of the credit you got in just one month of one idling demo).
