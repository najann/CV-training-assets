import os

import cv2
import numpy as np


COCO_FOLDER = os.path.sep.join(["yolo", "cvdetect", "yolo-coco"])


def initialize_net():

    weightsPath = os.path.sep.join(
        [COCO_FOLDER, "yolov3.weights"])
    configPath = os.path.sep.join(
        [COCO_FOLDER, "yolov3.cfg"])

    # load YOLO object detector trained on COCO dataset (80 classes)
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    return net


def process_image(image, net):

    # decode bytes of input image and grab spatial dimensions
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    global H, W
    (H, W) = image.shape[:2]

    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # construct a blob from the input image and then perform a forward
    # pass of the YOLO object detector, giving us our bounding boxes and
    # associated probabilities
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)
    return layerOutputs


def get_predictions(layerOutputs, confval=0.5, thresh=0.3):

    # initialize lists of detected bounding boxes, confidences, class IDs
    global boxes
    boxes = []
    global confidences
    confidences = []
    global classIDs
    classIDs = []
    global idxs
    idxs = []

    if len(layerOutputs) == 0:
        return None

    # loop over layer outputs and detections
    for output in layerOutputs:
        for detection in output:
            # extract the class ID and confidence of the current object detection
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # filter out weak predictions
            if confidence < confval:
                continue

            # scale the bounding box coordinates back relative to the
            # size of the image, keeping in mind that YOLO actually
            # returns the center (x, y)-coordinates of the bounding
            # box followed by the boxes' width and height
            box = detection[0:4] * np.array([W, H, W, H])
            (centerX, centerY, width, height) = box.astype("int")

            # use the center (x, y)-coordinates to derive the top and
            # and left corner of the bounding box
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))

            # update list of bounding box coordinates, confidences, class IDs
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            classIDs.append(classID)

            # apply non-maxima suppression to avoid weak, overlapping bounding boxes
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, confval, thresh)

    return idxs


def annotate_image(image, idxs, name):

    # load the COCO class labels our YOLO model was trained on
    labelsPath = os.path.sep.join([COCO_FOLDER, "coco.names"])
    with open(labelsPath) as labels:
        LABELS = labels.read().strip().split("\n")

    if W < 1000 or H < 1000:
        scale = 0.5
        fs = 2
    elif W > 3000 or H > 3000:
        scale = 3
        fs = 5
    else:
        scale = 2
        fs = 4

    # initialize a list of colors to represent each possible class label
    np.random.seed(80)
    COLORS = np.random.randint(0, 256, size=(len(LABELS), 3),
                               dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # ensure at least one detection exists
    if len(idxs) > 0:
        for i in idxs.flatten():
            # extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            # draw a bounding box rectangle and label on the image
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
            text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
            np.random.seed(0)
            cv2.putText(image, text, (x, y - np.random.randint(5, 30)), cv2.FONT_HERSHEY_SIMPLEX,
                        scale, color, fs)
    cv2.imwrite(os.path.sep.join(
        ["yolo", "cvdetect", "output", f"{name}_predicted.jpg"]), image)
