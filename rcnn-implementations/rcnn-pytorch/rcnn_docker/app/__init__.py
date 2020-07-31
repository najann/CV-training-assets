# package
from pyramid.config import Configurator
from pyramid.response import Response


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_route('analyze', '/analyze')
    config.add_route('delete', '/del/{filename}')
    config.add_static_view(name='static', path='app:static')
    config.scan('.views')
    return config.make_wsgi_app()
