FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD website/* /code/
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
