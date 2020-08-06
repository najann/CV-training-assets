from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import requests
import os
import numpy as np


BENTO_URL = 'https://bentoml-her0ku-mtu5njy5odi3mgo.herokuapp.com'


app = Flask(__name__)


@app.route('/', methods=['GET'])
def say_hello():
    return render_template('home.html')


@app.route('/analyze', methods=['POST'])
def classify():
    error = False
    image = request.files['unpredicted']
    name, ext = os.path.splitext(secure_filename(image.filename))
    # if ext.lower() not in ('.png', '.jpg', '.jpeg'):
    #     # let's have some fun
    #     return HTTPResponse(status=418)
    filename = secure_filename(image.filename)
    image.save(os.path.join('static', 'images', filename))
    # files = {'media': open('test.jpg', 'rb')}
    # requests.post(url, files=files)
    with open(os.path.join('static', 'images', filename), 'rb') as input:
        rqt = requests.post(BENTO_URL + '/predict', headers={'Content-Type': 'image/*'},
                            data=input.read())
    if rqt.status_code != 200:
        error = True
    return render_template('result.html', error=error, pred=rqt.text, filename=url_for('static', filename='images/' + filename))


@app.route('/del/<img>', methods=['GET'])
def delete_image(img):
    img = os.path.join('static', 'images', img)
    if os.path.exists(img):
        os.remove(img)
    return redirect(url_for('say_hello'))


if __name__ == '__main__':
    app.run(port=5001, debug=True)
