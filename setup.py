from setuptools import setup

setup(
    name='pytree',
    version='0.1',
    py_modules=['pytree'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pytree=pytree:pytree
    ''',
)
