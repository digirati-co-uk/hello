FROM alpine:3.6

RUN apk add --update --no-cache --virtual=run-deps \
  uwsgi \
  uwsgi-python3 \
  uwsgi-http \
  build-base \
  python3-dev \
  ca-certificates

ENV EXAMPLE_VARIABLE example_value

WORKDIR /opt/deployed
CMD [ "uwsgi", "--plugins", "http,python3", "--http", "0.0.0.0:3000", "--module", "hello" ]

COPY requirements.txt /opt/deployed/
RUN pip3 install --no-cache-dir -r /opt/deployed/requirements.txt

COPY *.py /opt/deployed/
COPY migrations /opt/deployed/migrations
COPY app /opt/deployed/app
