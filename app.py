import os

import numpy as np

from bottle import (
    default_app,
    get,
    post,
    request,
    run,
    static_file,
    template,
)
from yolo.cvdetect.yolo import (
    annotate_image,
    get_predictions,
    initialize_net,
    process_image,
)


IMAGE_FOLDER = os.path.sep.join(["yolo", "cvdetect", "images"])
PATH = os.path.abspath(__file__)
ROOT = os.path.dirname(PATH)

application = default_app()


@get('/')
def index():
    global net
    net = initialize_net()
    print(PATH, ROOT)
    return template('home')


@get('/styles/<filename:re:.*\.css>')
def send_file(filename):
    return static_file(filename, root=os.path.sep.join([ROOT, 'styles']))


@get('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root=os.path.sep.join([ROOT, 'styles', 'images']))


@get('/predictions/<filename:re:.*\.jpg>')
def send_result(filename):
    return static_file(filename, root=os.path.sep.join([ROOT, 'yolo', 'cvdetect', 'output']), mimetype='image/jpg')


@post('/analyze')
def localize_classify():
    error = False
    image = request.files.get('unpredicted')
    name, ext = os.path.splitext(image.filename)
    if ext.lower() not in ('.png', '.jpg', '.jpeg'):
        return 'File extension not allowed.'
    image = np.asarray(bytearray(image.file.read()), dtype="uint8")
    layers = process_image(image, net)
    idxs = get_predictions(layers)
    if len(idxs) == 0:
        error = True
    annotate_image(image, idxs)
    return template('result', error=error)


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, reloader=True)
