FROM python:3.8

RUN apt-get update
RUN apt-get install -y python3-dev default-libmysqlclient-dev

ARG PROJECT=haranathbasak
ARG PROJECT_DIR=/home/ubuntu/haranath_basak/

WORKDIR $PROJECT_DIR

COPY requirements.txt .

RUN pip3 install -r requirements.txt

ADD . $PROJECT_DIR

CMD [ "python3", "haranathbasak.py" ]