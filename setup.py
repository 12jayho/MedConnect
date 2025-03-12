from setuptools import find_packages, setup

setup(
    name='medibot',
    version='0.0.0',
    author='jay penshanwar',
    author_email='jaypenshanwar1812@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'streamlit',
        'transformers'
    ]
)
