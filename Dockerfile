FROM python:slim-stretch

# install dependencies
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /src
ADD frater/ frater/
ADD setup.py setup.py

RUN python setup.py install
WORKDIR /home

# clean up
RUN rm -rf /src

CMD ["python"]