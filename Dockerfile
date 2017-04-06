FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
ADD . /code/
WORKDIR /code/example

RUN python manage.py migrate
RUN python manage.py train

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
