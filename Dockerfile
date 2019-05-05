FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code/
RUN pip install -r /code/requirements.txt
WORKDIR /code/website
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
