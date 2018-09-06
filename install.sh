#!/bin/bash
cd ./wechatalert/
tar zcvf django.tar.gz ./
mv ./django.tar.gz ../
cd ../
docker build -t wechatalert ./
rm -rf ./django.tar.gz
