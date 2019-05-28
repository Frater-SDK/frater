FROM python:3.7.3-slim-stretch

# install dependencies
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD frater frater
ADD setup.py setup.py

RUN python setup.py install