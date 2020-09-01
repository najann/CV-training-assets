# Computer Vision with PyTorch

## FasterRCNN

PyTorch, resp. the `torchvision` library, provides pre-trained models for typical computer vision problems (i.e. the implementation of common, efficient architectures).

For the case of object detection, you can find a [FasterRCNN](https://pytorch.org/docs/stable/torchvision/models.html#faster-r-cnn) based on ResNet. It was trained to detect the COCO-2017 classes.
An example of its usage can be found [in this notebook](FasterRCNNPytorch.ipynb).

## Transfer Learning

The purpose of TL is to reduce the time spent on training different models on quite similar tasks.
Especially for image classification and object detection, neural nets often carve out the same low-level features no matter which subjects the images contain.
Therefore, you can pick up any pre-trained model and use it as a basis for your specific tasks.

To this end, you could fine-tune that base model, which means loading the existing parameters of all layers and improving them with a very small learning rate.
Alternatively, you can freeze the base model (parameters won't be updated in the backpropagation step) and extract the output of the second last layer as fixed features. The last fully-connected layer will be replaced by a new one. Then, this last classification layer is trained with the custom image dataset.

[This notebook](./TransferLearningPytorch.ipynb) shows you how to implement both options in PyTorch.

The custom dataset used is the [hymenoptera dataset](https://download.pytorch.org/tutorial/hymenoptera_data.zip), which should be extracted to `rcnn-pytorch/hymenoptera_data/`.
