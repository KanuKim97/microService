FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirement.txt /app/requirement.txt
RUN pip install -r requirement.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000