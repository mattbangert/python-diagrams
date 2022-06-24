
FROM python:3.9-alpine

LABEL maintainer="Matt Bangert <mattbangert@gmail.com>"

RUN apk update && apk add --no-cache graphviz \
  && rm -rf /var/cache/apk/* \
  && pip3 install diagrams

ENTRYPOINT ["python3"]
CMD ["-c", "print('Pass python script file path to container to create diagrams.')"]