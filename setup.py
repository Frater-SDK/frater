from setuptools import setup, find_packages

packages = find_packages(exclude=['tests*'])

dependencies = list(line.strip() for line in open('requirements.txt').readlines())

setup(
    name='frater',
    version='0.2.2',
    packages=packages,
    license='MIT',
    url='https://github.com/frater-sdk/frater',
    author='John Henning',
    author_email='john.l.henning@ibm.com',
    description='A Data-Driven Component System Framework and Toolkit',
    install_requires=dependencies,
    python_requires='>=3.7'
)
