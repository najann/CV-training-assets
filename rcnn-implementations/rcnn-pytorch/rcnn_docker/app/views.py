from pyramid.view import (
    view_config,
    view_defaults
)


# @view_config(route_name='home', renderer='home.jinja2')
# def home(request):
#     return {'name': 'Home View'}

#name = self.request.params.get('name', 'No Name Provided')


@view_defaults(renderer='home.pt')
class MainViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        filename = self.request.matchdict['file']
        # return {
        #     'filename': filename
        # }
