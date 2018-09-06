#!/bin/bash
tar zcvf django.tar.gz ./
docker build -t wechatAlert ./
rm -rf ./django.tar.gz
