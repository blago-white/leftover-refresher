FROM python:3.11.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update

RUN adduser -D -u 1000 refresher --home /home/refresher/

WORKDIR /home/refresher/

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chown -R refresher:refresher /home/refresher/
RUN chmod -R u+x /home/refresher/

USER refresher

CMD ["python", "loop.py"]
