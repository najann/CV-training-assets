from setuptools import setup

# List of dependencies installed via `pip install -e .`
# by virtue of the Setuptools `install_requires` value below.
requires = [
    'deform',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_jinja2',
    'waitress',
]

setup(
    name='app',
    install_requires=requires,
    packages=['rcnn'],
    entry_points={
        'paste.app_factory': [
            'main = app:main'
        ],
    },
)
