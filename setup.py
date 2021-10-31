from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='Anton K',
    author_email='kakkazak@gmail.com',
    description='FastApi app',
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
    ],
    scripts=['app/main.py']
)
