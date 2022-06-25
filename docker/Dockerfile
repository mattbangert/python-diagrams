
FROM python:3.9-alpine

LABEL maintainer="Matt Bangert <mattbangert@gmail.com>"

RUN apk update && apk add --no-cache graphviz=2.38.0-r5 \
  && rm -rf /var/cache/apk/* \
  && pip3 install --no-cache-dir diagrams==0.21.1

ENTRYPOINT ["python3"]
CMD ["-c", "print('Pass python script file path to container to create diagrams.')"]