from setuptools import setup, find_packages

packages = find_packages(exclude=['tests*'])
print(f'packages {packages}')

setup(
    name='frater',
    version='0.1.0',
    packages=packages,
    url='https://github.ibm.com/john-l-henning/frater',
    license='Apache 2.0 License',
    author='John Henning',
    author_email='john.l.henning@ibm.com',
    description='A Machine Learning System Framework and Toolkit',
    install_requires=[
        'requests',
        'flask',
        'grpcio',
        'grpcio-tools',
        'easydict',
        'numpy',
        'protobuf',
        'pyyaml',
        'kafka-python',
        'pillow',
    ]
)
