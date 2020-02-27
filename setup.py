from setuptools import setup, find_packages

packages = find_packages(exclude=['tests*'])

with open('requirements.txt') as f:
    dependencies = list(line.strip() for line in f.readlines())

with open('README.md') as f:
    description = f.read()

setup(
    name='frater',
    version='0.3.1',
    packages=packages,
    license='MIT',
    url='https://github.com/frater-sdk/frater',
    author='John Henning',
    description='A Machine Learning and Data-Driven Systems Framework and Toolkit',
    long_description=description,
    long_description_content_type='text/markdown',
    author_email='john.l.henning@ibm.com',
    install_requires=dependencies,
    python_requires='>=3.6'
)
