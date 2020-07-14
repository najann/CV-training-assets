import os

import numpy as np

from PIL import Image

from bottle import (
    default_app,
    error,
    get,
    HTTPResponse,
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


PATH = os.path.abspath(__file__)
ROOT = os.path.dirname(PATH)
IM_OUT = os.path.sep.join([ROOT, 'yolo', 'cvdetect', 'output'])
NET = initialize_net()

application = default_app()


@error(404)
def error_handler_404(error):
    return template('error', error='404')


@error(500)
def error_handler_500(error):
    return template('error', error='500')


@error(418)
def error_handler_418(error):
    return template('error', error='418')


@get('/')
def index():
    return template('home')


@get('/styles/<filename:re:.*\.css>')
def send_file(filename):
    return static_file(filename, root=os.path.sep.join([ROOT, 'styles']))


@get('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root=os.path.sep.join([ROOT, 'styles', 'images']))


@get('/predictions/<filename:re:.*\.jpg>')
def send_result(filename):
    return static_file(filename, root=IM_OUT, mimetype='image/jpg')


@post('/analyze')
def localize_classify():
    error = False
    confidence = float(request.forms.get('confidence'))
    thresh = float(request.forms.get('threshold'))

    image = request.files.get('unpredicted')
    name, ext = os.path.splitext(image.filename)
    if ext.lower() not in ('.png', '.jpg', '.jpeg'):
        return HTTPResponse(status=418, body=theBody)
    image = np.asarray(bytearray(image.file.read()), dtype="uint8")
    layers = process_image(image, NET)

    idxs = get_predictions(layers, confidence, thresh)
    if len(idxs) == 0:
        error = True
    annotate_image(image, idxs, name)
    optimize = Image.open(os.path.sep.join([IM_OUT, f"{name}_predicted.jpg"]))
    optimize.save(os.path.sep.join(
        [IM_OUT, f"{name}_predicted.jpg"]), optimize=True, quality=50)

    return template('result', error=error, file=f"/predictions/{name}_predicted.jpg")


if __name__ == '__main__':
    # run(host='0.0.0.0', port=8080, reloader=True)
    if os.environ.get('ON_HEROKU'):
        port = int(os.environ.get("PORT"))
    else:
        port = '8080'
    run(host='0.0.0.0', port=port, server='tornado')
