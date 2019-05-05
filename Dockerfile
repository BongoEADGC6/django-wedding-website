FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD requirements.txt /code/
ADD website/* /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
