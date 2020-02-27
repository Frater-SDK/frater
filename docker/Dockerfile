FROM python:slim-stretch


WORKDIR /src
ADD requirements.txt requirements.txt
ADD README.md README.md
ADD frater frater/
ADD setup.py setup.py

RUN python setup.py install
WORKDIR /home

# clean up
RUN rm -rf /src

CMD ["python"]