import os

import numpy as np
from PIL import Image

from bottle import (
    HTTPResponse,
    default_app,
    error,
    get,
    post,
    redirect,
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


ROOT = os.path.dirname(os.path.abspath(__file__))
IM_OUT = os.path.sep.join([ROOT, 'yolo', 'cvdetect', 'output'])
NET = initialize_net()

application = default_app()

######################
#   Error Handlers   #
######################


@error(404)
def error_handler_404(error):
    return template('error', error='404')


@error(500)
def error_handler_500(error):
    return template('error', error='500')

# a joke HTTP error but useful for wrong image upload formats
@error(418)
def error_handler_418(error):
    return template('error', error='418')


######################
#       Routes       #
######################

@get('/')
def index():
    return template('home')

# delete output files before returning to the home page
@get('/del/<filename:re:.*\.jpg>')
def del_image(filename):
    if os.path.exists(os.path.sep.join([IM_OUT, filename])):
        os.remove(os.path.sep.join([IM_OUT, filename]))
    redirect('/')

# stylesheets
@get('/styles/<filename:re:.*\.css>')
def send_file(filename):
    return static_file(filename, root=os.path.sep.join([ROOT, 'styles']))

# background image
@get('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root=os.path.sep.join([ROOT, 'styles', 'images']))

# return output file
@get('/predictions/<filename:re:.*\.jpg>')
def send_result(filename):
    return static_file(filename, root=IM_OUT, mimetype='image/jpg')

# process uploaded image
@post('/analyze')
def localize_classify():
    error = False
    confidence = float(request.forms.get('confidence'))
    thresh = float(request.forms.get('threshold'))

    image = request.files.get('unpredicted')
    name, ext = os.path.splitext(image.filename)
    if ext.lower() not in ('.png', '.jpg', '.jpeg'):
        # let's have some fun
        return HTTPResponse(status=418)

    # convert image to numpy array and send through YOLO net
    image = np.asarray(bytearray(image.file.read()), dtype="uint8")
    layers = process_image(image, NET)
    idxs = get_predictions(layers, confidence, thresh)
    # no objects detected ? cause error modal to pop up
    if len(idxs) == 0:
        error = True
    annotate_image(image, idxs, name)

    # optimize image size to improve loading time
    optimize = Image.open(os.path.sep.join([IM_OUT, f"{name}_predicted.jpg"]))
    optimize.save(os.path.sep.join(
        [IM_OUT, f"{name}_predicted.jpg"]), optimize=True, quality=50)

    return template('result', error=error, file=f"{name}_predicted.jpg")


if __name__ == '__main__':
    if os.environ.get('ON_HEROKU'):
        run(host='0.0.0.0', port=int(os.environ.get("PORT")), server='tornado')
    else:
        run(host='0.0.0.0', port=8080, reloader=True, debug=True)
