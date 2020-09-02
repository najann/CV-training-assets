# RCNNs with Keras

## :notebook: The Notebooks

[Keras_IMG_Classification.ipynb](./Keras_IMG_Classification.ipynb) is a very short notebook showing the unmodified usage of pre-trained keras appplication models for basic image classification.

As the name suggests, the notebook [TransferLearningKeras](./TransferLearningKeras.ipynb) shows step by step how to use a pre-trained Keras application model as a fixed feature extractor and fine-tune all layers in a second training loop. Moreover, it ...

- loads the cats/dogs tensorflow dataset
- applies some data augmentation
- does the transfer learning
- shows you different ways (i.e. formats) to save the model
- decodes the model's predictions item/batch-wise

[TensorflowJSmodel.ipynb](TensorflowJSmodel.ipynb) is structured similarly to [TransferLearningKeras](./TransferLearningKeras.ipynb). However, it skips the data augmentation and uses VGG19 as the underlying base model.
The main reason for that is that in order to be able to use the model in TensorflowJS it has to be built using Keras' Sequential API.
In combination with a transfer learning task, i.e. a fresh classification layer on top of a pre-trained model, VGG was the only architecture, which contained only those layers supported by TensorflowJS.

[RCNN_TF_Keras_OpenCV.ipynb](./RCNN_TF_Keras_OpenCV.ipynb) shows the implementation of a RCNN "from scratch".
It detects airplanes.

## Note in case of problems with jupyter:

```bash
pip install jupyter
pip uninstall notebook
pip install notebook
```

should solve **AttributeError: 'MappingKernelManager' object has no attribute 'connect_control'** according to [this link](https://github.com/jupyter/notebook/issues/2391#issuecomment-294732258)

A good overview: https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e
