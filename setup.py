from setuptools import setup

setup(
    name='frater',
    version='0.0.1',
    packages=['frater', 'frater.io', 'frater.core', 'frater.core.proto', 'frater.core.proto.core', 'frater.core.object',
              'frater.core.activity', 'frater.core.trajectory', 'frater.core.bounding_box', 'frater.core.frame',
              'frater.core.temporal_range', 'frater.task', 'frater.stream', 'frater.logging', 'frater.validation',
              'frater.utilities'],
    url='https://github.ibm.com/john-l-henning/frater',
    license='Apache 2.0 License',
    author='John Henning',
    author_email='john.l.henning@ibm.com',
    description='An Activity Detection SDK',
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
