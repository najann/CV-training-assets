import os

import numpy as np
import requests
from werkzeug.utils import secure_filename

from flask import Flask, abort, redirect, render_template, request, url_for


BENTO_URL = 'https://bentoml-her0ku-mtu5njy5odi3mgo.herokuapp.com'


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def say_hello():
        return render_template('home.html')

    @app.route('/analyze', methods=['POST'])
    def classify():
        image = request.files['unpredicted']
        filename = secure_filename(image.filename)
        name, ext = os.path.splitext(filename)
        if ext.lower() not in ('.png', '.jpg', '.jpeg'):
            # let's have some fun
            abort(418)
        image.save(os.path.join('tl-demo', 'static', 'images', filename))
        with open(os.path.join('tl-demo', 'static', 'images', filename), 'rb') as input:
            rqt = requests.post(BENTO_URL + '/predict', headers={'Content-Type': 'image/*'},
                                data=input.read())
        if rqt.status_code != 200:
            abort(500)
        return render_template('result.html', pred=rqt.text, filename=url_for('static', filename='images/' + filename))

    @app.route('/del/<img>', methods=['GET'])
    def delete_image(img):
        img = os.path.join('tl-demo', 'static', 'images', img)
        if os.path.exists(img):
            os.remove(img)
        return redirect(url_for('say_hello'))

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error.html', error=404), 404

    @app.errorhandler(418)
    def page_not_found(error):
        return render_template('error.html', error=418), 418

    @app.errorhandler(500)
    def page_not_found(error):
        return render_template('error.html', error=500), 500

    return app


if __name__ == '__main__':
    create_app()
