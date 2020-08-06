from PIL import Image

import bentoml
from bentoml.artifact import PytorchModelArtifact
from bentoml.handlers import ImageHandler
from torchvision import transforms


CLASSES = ['ant', 'bee']

# The transformations required to resize, crop, normalize the image
# so that it can be fed into the model for prediction
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


@bentoml.env(pip_dependencies=['torch', 'torchvision'])
# Defines the artifact that is used to deserialize the model
@bentoml.artifacts([PytorchModelArtifact('model')])
class AntOrBeeClassifier(bentoml.BentoService):

    # the actual api definition. Requires a ImageHandler to
    # accept the incomeing img.
    @bentoml.api(ImageHandler)
    def predict(self, img):

        # convert the image to pillow image for PyTorch
        img = Image.fromarray(img)
        # perform the transformations, returns a tensor (3, 224, 224)
        img = transform(img)

        # Use eval mode for evaluation.
        self.artifacts.model.eval()
        # Performs forward prop
        outputs = self.artifacts.model(img.unsqueeze(0))
        # find the index with the highest probability
        _, idxs = outputs.topk(1)
        idx = idxs.squeeze().item()
        # return the prediction
        return CLASSES[idx]
