FROM alpine:latest

RUN apk add python3 bash tcpflow

WORKDIR /app
ADD solution.py /app/

CMD /usr/bin/python3 solution.py
