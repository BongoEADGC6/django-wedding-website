FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r /code/requirements.txt
CMD ["python", "website/manage.py", "runserver", "0.0.0.0:8000"]
