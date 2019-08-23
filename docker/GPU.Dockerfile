FROM nvidia/cuda:10.1-cudnn7-runtime
MAINTAINER 'John Henning'

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.3.27-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda install python=3.7

# install dependencies
ADD ../requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /src
ADD ../frater frater/
ADD ../setup.py setup.py

RUN python setup.py install
WORKDIR /home

# clean up
RUN rm -rf /src

CMD ["python"]