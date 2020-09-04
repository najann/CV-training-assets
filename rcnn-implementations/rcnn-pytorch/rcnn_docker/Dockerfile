FROM python:3.7-slim

WORKDIR /app

RUN pip3 install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0 wget
COPY . /app
RUN mkdir -p /root/.cache/torch/checkpoints
RUN mv /app/rcnn/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth /root/.cache/torch/checkpoints/
EXPOSE 5000

RUN  set -e && python setup.py develop
CMD [ "python", "runapp.py" ]