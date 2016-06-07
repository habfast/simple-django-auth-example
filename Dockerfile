FROM python:3.5

MAINTAINER paul@ahead-solutions.ch

WORKDIR /root/

COPY requirements.txt /root/

RUN pip install -r requirements.txt

COPY manage.py /root/
COPY simpleauthexample /root/simpleauthexample/

CMD python manage.py runserver 0.0.0.0:8000
