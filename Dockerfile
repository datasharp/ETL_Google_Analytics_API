FROM python:3.9.7

RUN apt-get update

WORKDIR /code
COPY . /code


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]


