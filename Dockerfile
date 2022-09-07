FROM python:3.9

MAINTAINER passionsjin@hanwha.com

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

ENV PYTHONPATH /app

CMD ["python", "main.py"]