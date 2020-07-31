from pyramid.view import view_config
from pyramid.renderers import render_to_response
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPInternalServerError

import colander
import deform.widget
import os
import numpy as np
from rcnn import rcnn as rcnn
from PIL import Image

response = HTTPNotFound('There is no such resource')


class MainViews:
    def __init__(self, request):
        self.request = request
        self.css_url = self.request.static_url('app:static/main.css')

    @view_config(route_name='home')
    def home(self):
        action_url = self.request.route_url('analyze')
        return render_to_response('home.jinja2', dict(css_url=self.css_url, action_url=action_url), request=self)

    @view_config(route_name='analyze')
    def analyze(self):
        error = False
        name, ext = os.path.splitext(self.request.POST['unpredicted'].filename)
        if ext.lower() not in ('.png', '.jpg', '.jpeg'):
            return 'Sorry, not a supported file format'

            # let's have some fun
        # return HTTPResponse(status=418)
        upload = self.request.POST['unpredicted'].file
        image = np.asarray(bytearray(upload.read()), dtype="uint8")
        confidence = float(self.request.POST['confidence'])
        pred_box, pred_class = rcnn.get_prediction(image, threshold=confidence)
        if len(pred_box) == 0:
            error = True
        result = rcnn.make_result(image, name, pred_box, pred_class)
        optimize = Image.open(result)
        optimize.save(result, optimize=True, quality=50)

        return render_to_response('result.jinja2', dict(error=error, filename=result.split('/')[-1], css_url=self.css_url), request=self)

    @view_config(route_name='delete')
    def delete(self):
        if os.path.exists(os.path.sep.join(['app', 'static', 'outputs', self.request.matchdict['filename']])):
            os.remove(os.path.sep.join(
                ['app', 'static', 'outputs', self.request.matchdict['filename']]))
        return HTTPFound(location='/')
