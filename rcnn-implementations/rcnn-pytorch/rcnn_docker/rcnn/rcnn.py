import os

import cv2
import matplotlib as mpl
import numpy as np

import torch
import torchvision
from torchvision import transforms
from torchvision.models.detection import fasterrcnn_resnet50_fpn


mpl.use('Agg')


COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()
TRANSFORMS = transforms.Compose([transforms.ToTensor()])


def read_img(img):
    image = cv2.imdecode(img, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    return image


def get_prediction(img, threshold=0.5):
    image = read_img(img)
    img = TRANSFORMS(image)
    pred = model([img])
    pred_class = [COCO_INSTANCE_CATEGORY_NAMES[i]
                  for i in list(pred[0]['labels'].numpy())]
    pred_boxes = [[(i[0], i[1]), (i[2], i[3])]
                  for i in list(pred[0]['boxes'].detach().numpy())]
    pred_score = list(pred[0]['scores'].detach().numpy())
    try:
        pred_t = [pred_score.index(x) for x in pred_score if x > threshold][-1]
        pred_boxes = pred_boxes[:pred_t+1]
        pred_class = pred_class[:pred_t+1]
    except IndexError as ie:
        print(
            f'Sorry, no objects were detected that suit the threshold {threshold}')
        pred_boxes = []
        pred_class = []
    return pred_boxes, pred_class


def make_result(img, name, boxes, classes):
    import matplotlib.pyplot as plt
    image = read_img(img)
    COLORS = np.random.randint(0, 256, size=(
        len(np.unique(classes)), 3), dtype="uint8")
    pred_dict = dict(zip(np.unique(classes), COLORS))
    for i in range(len(boxes)):
        color = tuple(int(c) for c in pred_dict[classes[i]])
        cv2.rectangle(image, boxes[i][0], boxes[i][1], color, thickness=3)
    plt.figure(figsize=(10, 20))
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])
    markers = [plt.Line2D([0, 0], [0, 0], color=color/255,
                          marker='o', linestyle='') for color in pred_dict.values()]
    plt.legend(markers, pred_dict.keys(), numpoints=1)
    path = os.path.join('app', 'static', 'outputs', f'{name}.jpg')
    plt.savefig(path, bbox_inches='tight')
    return path
