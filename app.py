from bottle import get, post, request, run, template
from yolo.cvdetect.yolo import initialize_net, process_image, get_predictions, annotate_image
import os


# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

IMAGE_FOLDER = os.path.sep.join(["yolo", "cvdetect", "images"])


@get('/')
def index():
    global net
    net = initialize_net()
    return template('home')


@post('/loClas')
def localize_classify():
    image = request.files.get('unpredicted')
    name, ext = os.path.splitext(image.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return 'File extension not allowed.'
    image.save(IMAGE_FOLDER, overwrite=True)
    layers = process_image(os.path.sep.join(
        [IMAGE_FOLDER, "CasperFFM17.jpg"]), net)
    print(layers)
    idxs = get_predictions(layers)
    print(idxs)
    annotate_image(os.path.sep.join(
        [IMAGE_FOLDER, "CasperFFM17.jpg"]), idxs)

    return ('Image uploaded')


run(host='0.0.0.0', port=8080)
