# A FastAPI For The TFJS Model

_Date: 08/2020_

## Get The TFJS Model

[./model-tfjs-layer](model-tfjs-layer) contains a trained keras model which was converted to tensorflowJS format:

1. Save you model using `model.save('model.h5')`.
2. Use the tfjs-converter to build a tfjs-formatted model: `tensorflowjs_converter --input_format keras model.h5 model-tfjs-layer`.
   - The output directory will contain a bunch of binary files and a model.json which represents your model's architecture.
   - [https://www.tensorflow.org/js/tutorials/conversion/import_keras](Documentation)
   - _Note:_ I tried several times to use the Python API to save the keras model in tfjs-format directly. However, the output never worked correctly.

### Remarks

You may tend to skip this paragraph but the following part from the documentation may save you quite some time:

```txt
TensorFlow.js Layers currently only supports Keras models using standard Keras constructs. Models using unsupported ops or layers—e.g. custom layers, Lambda layers, custom losses, or custom metrics—cannot be automatically imported, because they depend on Python code that cannot be reliably translated into JavaScript.
```

This means that you also cannot include layers from `tensorflow.keras.layers.experimental` (such as the image preprocessing layers).
Similarily, I could not use the pre-trained MobileNet/Inception/Xception nets because they are implemented using keras' functional API.
However, tfjs apparently only accepts models built using the sequential API.
Consequently, I had to retrieve every layer from the pre-trained models (except the `InputLayer` and top layer), add it to a sequential model in between the custom layers I used for transfer learning purposes and compile/fit that.

### Evaluation

TFJS is an interesting offer to have a look at in terms of edge computing.
However, as also mentioned in some articles, you have to bear in mind that users may get access to your model's definition.
Therefore, TFJS seems to be fine for small private projects or public ones where nothing's at risk if you provide access to your model.
On the other hand, I feel like TFJS has a considerable amount of pitfalls - e.g. which layers you can use, how to convert the format, etc. - as soon as you don't want to stick with the provided models but build your own ones or do some transfer learning.

(I did not try to build a model in JavaScript itself. Maybe this is easier than transferring it from Python code.)

## Serve Your Model Files Via FastAPI

### Creating An App

This demo uses FastAPI to serve the `model.json` and binary files (in subdirectory [model-tfjs-layer](./model-tfjs-layer)).
It is a very small app and is defined in [./main.py](main.py).
There are only two API endpoints: the entry point `/`, which returns the main `model.json` file, and `/group1-shardXofY.bin`.
Subsequent to `model.json`, the latter is automatically called by the JS function `tf.loadLayersModel()` until it retrieved Y of Y shards.

## Dockerizing The App

The [Dockerfile](./Dockerfile) in this subdirectory uses a base image provided by the team behind FastAPI.
So, all you have to add are ancillary libraries and the app's code.
