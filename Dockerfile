FROM python:3.7.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY flask_app/ /app/

EXPOSE 5090

CMD ["python", "app.py"]
