FROM python:3.7.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /flask_api
WORKDIR /flask_api

COPY requirements.txt /flask_api/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY flask_api/ /flask_api/

EXPOSE 5090

CMD ["python", "app.py"]
