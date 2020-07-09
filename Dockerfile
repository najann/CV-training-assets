FROM python:3.7-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip
# needed so that opencv works correctly 
# import cv2
# File "/usr/local/lib/python3.7/site-packages/cv2/__init__.py", line 5, in <module>
# from .cv2 import *
# ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file or directory
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0
RUN pip3 install -r requirements.txt
EXPOSE 8080

COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]