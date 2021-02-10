FROM python:3.7.2

ENV PYTHONUNBUFFERED 1


RUN mkdir /app
WORKDIR /app


COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY flask_app/ /app/

EXPOSE 5090

ENV MESSAGE "hello from Docker"

ENTRYPOINT ["python"]
CMD ["app.py"]
