FROM alpacamarkets/marketstore:v2.1.2

# adding bash util
RUN apk add --update bash && rm -rf /var/cache/apk/*

RUN mkdir -p /project/data/mktsdb

COPY . /project