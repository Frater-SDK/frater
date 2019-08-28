from setuptools import setup, find_packages

packages = find_packages(exclude=['tests*'])
setup(
    name='frater',
    version='0.2.0',
    packages=packages,
    url='https://gitlab.com/diva-phase-2/frater',
    author='John Henning',
    author_email='john.l.henning@ibm.com',
    description='A Machine Learning System Framework and Toolkit',
    install_requires=[
        'flask',
        'requests',
        'easydict',
        'numpy',
        'pyyaml',
        'kafka-python',
        'pillow',
    ]
)
