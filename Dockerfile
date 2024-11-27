FROM python:3.11.4-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./core .
CMD ["python","manage.py","runserver","0.0.0.0:8000"]