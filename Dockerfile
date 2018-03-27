FROM ubuntu:14.04
MAINTAINER Sami Moustachir <moustachir.sami@gmail.com>

ENV https_proxy=http://10.244.16.9:9090
ENV http_proxy=http://10.244.16.9:9090

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

RUN apt-get update && apt-get install -y \
        build-essential \
        wget \
        python python-dev \
        python-pip \
        python-virtualenv \
        automake

COPY . /app

RUN pip install -r app/requirements.txt

RUN cd app && \
    mkdir -p data && \
    wget https://gforge.inria.fr/frs/download.php/file/36209/melt-2.0b12.tar.gz\
    && tar -zxvf melt-2.0b12.tar.gz \
    && cd melt-2.0b12 \
    && aclocal  \
    && autoconf \
    && automake -a \
    && ./configure \
    && make \
    && sudo make install

VOLUME /app/data

WORKDIR /app/melt_app/src

CMD ["python", "melt_app.py"]
