FROM alpine:3.6

RUN apk add --update --no-cache --virtual=run-deps \
  uwsgi \
  uwsgi-python3 \
  python3 \
  nginx \
  ca-certificates

ENV EXAMPLE_VARIABLE example_value

WORKDIR /opt/deployed
CMD ["/opt/deployed/run.sh"]

COPY run.sh /opt/deployed/
RUN chmod +x /opt/deployed/run.sh

COPY etc/nginx/default.conf /etc/nginx/conf.d/

COPY requirements.txt /opt/deployed/
RUN pip3 install --no-cache-dir -r /opt/deployed/requirements.txt

COPY *.py /opt/deployed/
COPY migrations /opt/deployed/migrations
COPY app /opt/deployed/app
